# Instagram Ad-hoc Analysis

You are a data analyst at an NYC-based wholesale food supplier called Osiris-Foods. As part of your companies mission to make more data-driven decisions, you are tasked with generating an ad-hoc report on your companies database. You will report on descriptive statistics using SQL and generate respective visualizations using pandas to provide your company an overview of its' past performance.

For this project, you will analyze an ERD diagram to formulate DML SQL queries within a Jupyter notebook, and provide a write-up of your findings. 

Keep in mind that your write-up should include pertinent numerical details to back your findings. Any claim that you make must be supported by evidence!

## Instructions

### Market.db

Before beginning your project, we recommend checking out the ERD diagram below:

![ERD Diagram](/images/Northwind_E-R_Diagram.png)  
*ERD Diagram of Market Database*

Use this ERD diagram to formulate how you should form your joins across tables and to find out more about your table's columns.

If you download the `sqlite3` VSCode extension, you will also be able to open your database within your code editor to view the content and columns of your table.

Note that you can also test out your SQL queries in `sqlite3` by opening your database in your command line or terminal. Check out the [guide](https://datacarpentry.github.io/sql-socialsci/instructor/08-sqlite-command-line.html) for more information on how to interact with your database in the shell.

### adhoc_report.ipynb

Within this Jupyer notebook, you will write Python code and SQL queries to answer 8 ad-hoc questions. Each question will involve you creating an appropriate DML SQL query and observing this output.

After you've verified that your query's output sufficiently answers the question, you will then create a pandas dataframe using this output and finally generate a visualization from this dataframe.

Just as in the `weather-analysis` project, we will not directly indicate which visualizations you should make. Instead, we ask that you use your notes and study material to discern appropriate visualizations.

Test your queries in the shell, and be sure to *iteratively* build your queries. Especially when we are first learning SQL, we rarely come up with an immediate answer. Start with your basic structure (`SELECT ... FROM ...`) and build up to the correct answer.

## Submission 

Your first checkpoint for this project will be due by `6/20`. The final due date for this project is `6/27`. 

To begin work on this project, you will download this template code and push it to your GitHub repository. 

While there are no tests for this project, be sure to remove all errors from your code before submitting and ensure that the outputs you generate answer each question. 

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

