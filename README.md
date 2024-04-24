This is the readme file for our SSW555 Project. In this project we take brain scan data and develop software to display the brain information.

This is first achieved by takign the information gathered from brain scans to the cloud.
Next we take that data and process it with developed algorithims for visualization.
We then use this processed data to display the active brain areas using our developed UI.
We believe that this tool can be used to help understand the human brain and how it works.
You can look into the repo and find our work there.

Sprint 1:
In sprint 1 our goal was to test and execute data preprocessing functions. 
To do this we installed the preprocessing code and ran python unit tests on different functions.
We ran most of our tests on the normalization and import functions.
These tests can be found in the main directory, with the preprocessing code found in the "data_preprocessing.ipynb

Sprint 2:
In sprint 2 we now want to apply our algorithims for data processing and visualization.
To do this we take the data and process it through the normalization and reshaping functions.
We then use this data to being visualization in the next sprint.
These files can be found in the main repo.

Sprint 3:
In sprint 3 we now plan our UI elements, continue testing, and implement our 3d visualization system.
To do this we take our processed data and pass it through the brain3d function, which utilizes MNE Visualization tools to visualzie our data.
We then plan to have this visualization accessible through a UI that we are currently planning.
This sets us up for our final goal of having a UI integrated tool for brain visualization, that allows the user to both view brain data and upload brain data files to be visualized.
The updated files can be found in the main repo.


![image](https://github.com/msavino16/SSW555-Group22/assets/149920321/a43fa80b-a314-43ed-9785-a49ebfb32d41)

Sprint 4:
In sprint 4 we now finalize all of our code elements, continue testing, and develop a website to host our data visualization.
To do this we are using a server to host our website, that will take our jupyter notebooks that provide our visualization, and make them available to be seen with a UI online.
We are attempting to use a flask server for this, as it can host a python server for us to use as our website base
We then develop a UI using basic CSS and React, so that the page may be interacted with
The updated code can be found in the main repo.
