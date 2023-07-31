# hb_conc

This repository has all the different codes written throughout the project.

## Trends identified so far:
+ For increasing concentration, there is a decrease in the peak intensity values of Blue Channel, Green Channel; an increase in the peak values of Saturation Channel. Observations from other features are unreliable or not consistent.
+ Another way of finding trends could be to find peak values of the least concentration value available and find the number of pixels available at those intensities for all available concentrations.

## Problems:
+ Insufficient data collected.
+ The data we have analysed with so far has not been collected with the same camera settings. There has always been some change in the settings that has led to data not following trends consistently.

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

### app.py
`app.py` has the script for the dashboard. This reads the mastercsv.
+ There is an input field that is not connected to anything.
+ After input field, you see a table that has all the data from the mastercsv.
+ Finally, you have the peak values and max number of pixels at an intensity of each channel for each image. Average of the peak values of the image are not taken.

### prep_img.py
`prep_img.py` takes the Date folder that has subfolders of concentrations available with images in each.

### crop_img.py
`crop_img.py` crops the image in the concentration subfolders to 900x900

### models.ipynb
This is a notebook created that checks mutual information of available features and target (concentration value).
According to me, based on the results, the features with mutual information > 1 are overfit. Path and pkPxls_G got values > 1.

To run the whole process:
+ There should be a date folder that has subfolders of all concentration, that have only images in them.
+ Copy date folder path in `prep_img.py` and `crop_img.py` and run the scripts individually.
+ Copy path of the date folder and paste it in `main_individual.py`.
+ Run `main_individual.py`.
+ Run `mastercsv.py`.
+ Run `app.py`.
+ In order to reset the data the is displayed on app.py, you have to delete the master.csv that is created.

# Roadblocks:
+ Deployment is pending.
+ Input field does not accept input.
+ Button is yet to be created on dashboard.
+ Data collection rate is very slow.
+ Insufficient data is collected, and trends are not being identified with images clicked yet. Some concentration images are not following trend.
