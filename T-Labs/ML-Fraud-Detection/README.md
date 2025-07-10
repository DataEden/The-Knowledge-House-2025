# Detect-Fraud

You are a data scientist working for a Zurich-based international bank called Caishen. The company announced in an all-hands meeting that the goal for the next 3 years will be to identify 99% of all fraudulent activity within their customer-facing bank accounts. While your cybersecurity team has provided you with a dataset of historic fraudulent activity, the responsibility of designing a minimal machine learning model has fallen on your desk. 

For this project you will use a dataset of 1 million bank transactions to create a classifier that will detect if fraudulent activity has occurred for a transaction. 

A problem that often occurs in the domain of fraud detection is [class imbalance](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets). We can assume that an overwhelming majority of transactions are credible and therefore "achieve" 99% accuracy simply by classifying every new sample as non-fraudulent (0). However, if we do this, we will miss every single fraudulent transaction and subsequently get a sensitivity of 0%. 

Within this project, you will create a comprehensive machine learning pipeline that utilizes the strategies we discuss in class to achieve non-zero precision, recall, and sensitivity. You will achieve this by doing the following:

* form a hypothesis through EDA, 
* complete data pre-processing, 
* and conclude with model generation and hyperparameter search.

## Data Dictionary

This dataset contains a mix of categorical and numerical variables. The data-dictionary below describes what each column represents:

* Type: The type of transaction   
* Amount: The amount of money transferred   
* NameOrig: The origin account name  
* OldBalanceOrg: The origin accounts balance before the transaction 
* NewBalanceOrig: The origin accounts balance after the transaction   
* NameDest: The destination account name   
* OldbalanceDest: The destination accounts balance before the transaction 
* NewbalanceDest: The destination accounts balance after the transaction 
* IsFlaggedFraud: A “naive” model that simply flags a transaction as fraudulent if it is greater than 200,000 (note that this currency is not USD)   
* IsFraud: Was this simulated transaction actually fraudulent? In this case, we consider “fraud” to be a malicious transaction that aimed to transfer funds out of a victim’s bank account before the account owner could secure their information. (This will be your target variable)   

Note that not all variables are important for this prediction task. Namely, all bank accounts are susceptible to being targets of fraudulent activity, so we most likely want to remove all columns that identify bank account information, and solely observe numerical predictors.

## Instructions

There are three Python notebooks that you will complete in this repository to complete this project:
* eda.ipynb
* transform.ipynb
* model_train.ipynb

Throughout each notebook, you will answer a set of analytical questions.

Further directions for each file are listed below: 

### eda.ipynb

Your project should begin with a notebook where you perform univariate, bivariate, and multivariate exploratory analysis on your dataset. Much like the `weather-analysis` project, we will not explicitly state which visualizations you should generate. Instead, we will provide you with a set of analytical questions which you will use to inform your feature engineering & model training.

**Univariate Analysis**
* Take a closer look at the numeric features in your dataset. How are these values distributed and what might this tell you about how most transactions behave compared to a few **rare** ones?

**Bivariate Analysis**
* When comparing different numerical features against one another, do any interesting patterns emerge for transactions marked as fraudulent? Are there particular regions or ranges where these transactions seem to concentrate?  
* How do types of transaction relate to the typical amounts involved? Are some types of transactions consistently larger or smaller than others?
* Do transaction amounts vary when you compare fraudulent and non-fraudulent transactions across different transaction types? What patterns emerge when you look at both fraud status and transaction type together?  
* Consider how well the system's built-in fraud flag (`isFlaggedFraud`) aligns with actual fraudulent activity. Are there mismatches? What does this tell you about the system's current performance?  


### transform.ipynb

After completing `eda.ipynb` you will use your EDA findings to prepare your dataset for machine learning.

While we will not tell you which operations to apply, we will ask you to consider a set of questions and apply appropriate transformations based on your decisions.

Use your classroom notes, recordings, and labs to answer these questions and apply data transformations.

**Data Transformation Questions**
* Does your model contain any missing values or "non-predictive" columns? If so, which adjustments should you take to ensure that your model has good predictive capabilities?
* Do certain transaction types consistently differ in amount or fraud likelihood? If so, how might you transform the type column to make this pattern usable by a machine learning model?
* After exploring your data, you may have noticed that fraudulent transactions are rare compared to non-fraudulent ones. What challenges might this pose when training a machine learning model? What strategies could you use to ensure your model learns meaningful patterns from the minority class?
* Are there interaction effects between variables (e.g., fraud and high amount and transaction type) that aren't captured directly in the dataset? Would it be helpful to manually engineer any new features that reflect these interactions?
* (Bonus/Optional) Are there interaction effects between variables (e.g., fraud and high amount and transaction type) that aren't captured directly in the dataset? Would it be helpful to manually engineer any new features that reflect these interactions? 

### model_train.ipynb

Now that you’ve pre-processed your dataset, it’s time to train and evaluate a machine learning model to predict fraudulent transactions.

While we won't walk you through each line of code, we will remind you of the typical steps we follow in the machine learning pipeline.

Additionally, we will not direct you towards one machine learning model or another. Instead, you will consider your prediction task and make an executive decision as to which model "makes sense" by considering the following questions.

**Model Selection Questions**
* Is this a classification or regression task?  
* Are you predicting for multiple classes or binary classes?  
* Given these observations, which 2 (or possibly 3) machine learning models will you choose?  

After selecting your models, you will follow the steps listed in the notebook. Use your classroom notes, recordings, and labs to answer questions and create ML models.

## Submission 

The due date for this project is `7/22`.

The first checkpoint is due `7/9` and the second checkpoint is due `7/16`. Check out your respective Canvas page to find out more about checkpoint details.
 
To submit this project, you will submit a link to your completed GitHub repository to Canvas.

