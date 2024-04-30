from flask import Flask, request, jsonify
from flask_cors import CORS
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

app = Flask(__name__)
CORS(app)  # Apply CORS to all routes and methods

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/run-notebook', methods=['POST'])
def run_notebook():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return 'No file part', 400

        file = request.files['file']

        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file', 400

        if file:
            # Save the uploaded file to the upload folder
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            
            # Open the Jupyter notebook
            with open('main.ipynb', 'r') as f:
                nb = nbformat.read(f, as_version=4)

            # Set up a notebook processor and execute the notebook
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': './'}})  # Adjust the path if your notebook uses files from specific paths

            # Save the executed notebook
            with open('main_executed.ipynb', 'wt') as f:
                nbformat.write(nb, f)
            
            # Delete the uploaded file
            os.remove(file_path)

            return 'Success!'
    except Exception as e:
        # Return the error message and a 500 Internal Server Error status
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all network interfaces and on port 5000
