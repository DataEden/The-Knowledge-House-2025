# Health Monitoring Data Processing

You are a software developer at a Taiwan-based wearable health-tech firm called Seng-Links. For your next project, you will assist in the creation of an application which will ingest 8 hours of user inputted heart-rate data and rate their quality of sleep. As the final project will take many months of hardware and software development, you are tasked with solely designing a simple application which developers can use to prototype to product. 

You will develop an analysis that identify periods when a user sleeps or exercises using their varying recorded heart rates. 

Your company has provided you a folder named "data/", which contains 4 files of heart-rate samples from a participant. The participants device records heart rate every 5 minutes (aka sampling rate). You are tasked with writing code that processes each data file. Note that some of these files contain erroneous data that you must filter out before performing your analysis and visualization. You will utilize test-driven development in order to complete this project.

## Instructions

First, to install the `matplotlib` library to your environment, run the following command in your VSCode terminal:

```
pip install matplotlib
```

There are three Python files which you will modify in this repository to complete this project:
* cleaner.py
* metrics.py
* main.py
* writeup.md

The files with the prefix `test_` (i.e. `test_clean.py`, `test_metrics.py`, and `test_run.py`) are intended for you to test your code to ensure that all project requirements are complete. **Do not modify the code in these files. Otherwise, you will not be able to check that your code is functioning correctly.**. 

Once you've completed the coding portion of this project and ensured that all output is correct, you will then provide a writeup in the file ` writeup.md`, where you will answer analytical questions on the data you've analyzed.

Further details and usage of each file are listed below: 

**cleaner.py**

This module contains a function you will implement to clean a list of data. `filter_nondigits` will take in a list of strings and filter out all strings that include non-digit characters. Remove the new-line character (`\n`) before performing this digit check! After validating that a string is a valid digit, you will convert this element into an integer and append it into a new list, which will be returned when your function ends.

To test this module open a terminal in VSCode. Go to the Terminal tab in the top menu and select "New Terminal." Then type the following command:

```
python test_cleaner.py
```

We recommend working on this module **first**. Be sure to write up a docstring when you've completed this function!

**metrics.py**

This module contains three functions that you will implement to calculate various descriptive statistics on your data. For example, the `average` function, you will calculate the average heart value of all input data.

You will apply this concept to calculate the maximum, variance, and standard deviation (do you recall what ties variance and standard deviation together?). As these functions will only be called **after** you've cleaned and removed outliers, you can expect your list of data to be integers. Be sure to round all floating point values to 2 decimal points!

To test this module on all possible inputs, you will run the following command in your terminal:

```
python test_metrics.py
```

**NOTE**: You must implement all statistical formula using base Python, and you cannot use modules which calculate these metrics for you (e.g. `stats.std()`). Furthermore you should use **for-loop** for both average and maximum to calculate the average and maximum respectively.

**main.py**

You can execute the following command in your terminal to run this file:

```
python main.py
```

By default, we include the path to the `phase0` text file if you want to test one file at a time. After running this module, view the figures created in your `images/` directory. This filepath is found underneath the conditional `if __name__ == "__main__":` and can be modified.

However, to test this module on all your available data files, you will run the following command in your terminal:

```
python test_run.py
```

This file will combine all previously implemented modules to clean, process, and visualize your data. This module will also utilize file I/O to read and save your data into a list. We recommend working on this file **last**.

**writeup.md**

This file contains 4 analytical questions you will answer based on the metrics and visualizations your code generates. Remember that you can manually develop the specified data visualizations by running your `main.py` file.

## Submission 

The due date for this project is `03/28`.

To begin work on this project, you will create a repository in your GitHub and copy all these template files into your repo.

Be sure to test as you code in order to verify that your functions are working correctly. If you see that all of your tests are evaluating to a green check-mark (✅) for a specific module, that means your code is ready to go, and you can move on to the next challenge.

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

