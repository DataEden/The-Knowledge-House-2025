# Weather Data Analysis

You are a data engineer at a Brazil-based weather prediction startup called Curu-Sight. The goal of this startup is to analyze weather trends in Brazil and predict the output of non-durable consumer goods at harvest time.

One major threat (barring tariffs) to Brazil's biggest export, coffee, is leaf rust. This fungus thrives in humid environments and causes plants to wither. Your company recently won a contract with the local government of Minas Gerais to analyze how humidity (and auxiliary measures) determine the yearly output of coffee.

You will analyze a dataset that contains averages calculated based on rainfall, temperature, humidity, and wind metrics collected during the coffee growing season. You will also analyze a dataset that contains Minas Gerais' crop output. You will then combine these two datasets to explore how the weather influences coffee growth.

## Data Dictionary

Column descriptions for each dataset is listed below:

**weather_data**
This dataset describes yearly weather outcomes for the coffee-growing months of Minas Gerais. Only weather data from January through May is considered.

* year: Year on which metrics were calculated. 
* rain_max: Average maximum millimeters of rain.
* temp_avg: Average temperature in celsius.
* temp_max: Average maximum temperature in celsius.
* temp_min: Average minimum temperature in celsius.
* hum_max: Average maximum humidity in percentage.
* hum_min: Average minimum humidity in percentage.
* wind_max: Average maximum wind speed in meters per second.
* wind_avg: Average wind speed in meters per second.
* subdivision: Name of Brazilian sub-division (all should be Minais Gerais)

**coffee_output**
This dataset describes yearly features related to the coffee harvest that begins in June and ends in September in Minas Gerais.

* country: Country where harvest occurs (all should be Brazil).
* subdivision: Name of sub-division (all should be Minais Gerais)
* type: Type of coffee bean
* 60kgs_bag: 60 kg bags of coffee beans harvested (million bags)
* year: Year of harvest
* nonbearing_trees: Amount of nonbearing coffee trees (million trees)
* bearing_trees: Amount of bearing coffee trees (million trees)
* nonbear_hectares: Hectares of nonbearing coffee trees (thousand hectares)
* bearing_hectares_per_hectare: Average number of bearing trees per hectare
* nonbearing_trees_per_hectare: Average number of non-bearing trees per hectare

## Instructions

There are three Jupyter notebooks which you will complete:
* notebooks/explore_weather.ipynb
* notebooks/explore_coffee.ipynb
* notebooks/analysis.ipynb

Each notebook entails a "write-up" section where you will document your findings. Further directions for each file are listed below: 

### explore_weather.ipynb

You will perform exploratory data analysis on `weather_data1.csv` and `weather_data2.csv`. Keep in mind that these files are essentially the same dataset with homogenous columns, but split into two files. Could you figure out a way to coalesce these files back together before beginning this analysis? Once you join these data files back together, you should save this resultant file into a new csv called `weather_data.csv`. 

Unlike previous exercises, we will **not** tell you which visualizations or metrics you should make. Instead, you should use the notes, slides, and recordings from week 6, week 7, and week 8 to figure out which visualizations you should generate to answer the following analytical questions below:

**Univariate Analysis**
* How is average temperature, minimum humidity, and average wind speed changing across the years for Minas Gerais? Is this increasing or decreasing?
* Which year had the highest maximum record rainfall?

**Bivariate Analysis**
* What is the relationship between max rain and max humidity? How *strong* is this relationship? Use pearson's correlation coefficient.
* What is the relationship between average wind speed and average temperature? How *strong* is this relationship? Use pearson's correlation coefficient.

### explore_coffee.ipynb

Next, you will perform exploratory data analysis on the `coffee_output.csv` file. This file contains some rows that contain null values. We should remove these rows before progressing with our EDA.

Furthermore, notice that we have other subdivisions in this dataframe. How can we filter out these other rows to only include **Minas Gerais**?

Create visualizations and metrics to answer the following analytical questions below:

**Univariate Analysis**
* How is bearing_trees, bearing_hectares, and 60kgs_bag changing across the years in Minas Gerais? Are these variables increasing or decreasing? 
* What is the distribution of bearing_trees, bearing_hectares, and 60kgs_bag in Minas Gerais? Do these variables follow a normal distribution?

**Bivariate Analysis**
* What is the relationship between bearing_trees and 60kgs_bag in Minas Gerais? How *strong* is this relationship? Use pearson's correlation coefficient.
* What is the relationship between bearing_hectares and 60kgs_bag in Minas Gerais? How *strong* is this relationship? Use pearson's correlation coefficient.

### analysis.ipynb

Lastly, you will join your `weather_data.csv` and `coffee_output.csv` files on the `year` and `subdivision` columns to explore how weather patterns correlate with coffee harvest output.

Create visualizations and metrics to answer the following questions:

**Bivariate Analysis**
* What is the relationship between temp_avg and 60kgs_bag? How *strong* is this relationship? Use pearson's correlation coefficient.
* What is the relationship between minimum humidity and 60kgs_bag? How *strong* is this relationship? Use pearson's correlation coefficient.
* What is the relationship between rain_max and 60kgs_bag? How *strong* is this relationship? Use pearson's correlation coefficient.
* What is the relationship between average wind speed and 60kgs_bag? How *strong* is this relationship? Use pearson's correlation coefficient.
* Perform the same bivariate analysis between the mentioned weather columns (temp_avg, hum_min, rain_max, and wind_avg) and a coffee-related column of your choice (bearing_trees, nonbearing_trees, bearing_trees_per_hectare, etc). Which directions do these relationships follow? What are the strengths of these relationships?
* Which weather factor seems to influence coffee production the most? 
* Which data would you collect to continue exploring the impacts of weather and economic forces on coffee production?
* If you were preparing a report to provide to coffee farmers, which weather condititions would you state are the most favorable for coffee growing (assuming any exist)?

## Submission 

The due date for this project is `5/14`.

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

**Note**: No one should have the same EDA. Remember, EDA is a self-guided process. If your EDA looks identical to another fellow's (or to ChatGPT's) your submission will receive a zero until you submit an original EDA.


