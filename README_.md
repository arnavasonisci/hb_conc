# hb_conc

This repository has all the different codes written throughout the project.

## Data Collection

### myimports.py

This has all the required library and package imports.

### histograms.py

A script to create histograms.

### Conc.py & main.py

This code has a class `Conc.py` that has multiple functions/methods for different calculations. There are multiple attributes that store the return values of the methods.
The `main.py` has the paths of the image folders, instance initializations, method calls, and code to make a figure with subplots that compare the histograms of different channels of BGR, HSV and CIE Lab.
It also creates a .csv file to store all the data.

The features in the .csv are:
+ peak intensity values in each channel after the histogram is plotted.
+ number of pixels at those peak points
+ the number of pixels in each image at the peak intensity of each channel`s histogram for the lowest concentration available.

### conc_Individual.py & main_individual.py

This `conc_Individual.py` has a class that has an attribute for the folder of the concentration image, a list that holds 10 dictionaries; each dictionary for an image of the concentration that has the same features as created in `Conc.py`, as key-value pairs.
`main_individual.py` has variables that store the image folders that are dedicated to each concentration and create a number of objects that are the same as the number of concentrations available. Here, histograms are not created, but a CSV that contains all the data in a tabular format is available.

`px_at_Peaks.py` does the same as "the number of pixels in each image at the peak intensity of each channel`s histogram for the lowest concentration available", but is not used.

### mastercsv.py
`mastercsv.py` has the csv where all the data stored is collected. This is the data visible on the `app.py` dashboard.
