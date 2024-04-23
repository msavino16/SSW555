from flask import Flask
from flask_cors import CORS
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

app = Flask(__name__)
CORS(app)  # Apply CORS to all routes and methods

@app.route('/run-notebook', methods=['POST'])
def run_notebook():
    try:
        # Open the Jupyter notebook
        with open('main.ipynb', 'r') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Set up a notebook processor and execute the notebook
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': './'}})  # Adjust the path if your notebook uses files from specific paths
        
        # Save the executed notebook
        with open('main_executed.ipynb', 'wt') as f:
            nbformat.write(nb, f)
        
        return 'Notebook executed successfully!'
    except Exception as e:
        # Return the error message and a 500 Internal Server Error status
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all network interfaces and on port 5000
