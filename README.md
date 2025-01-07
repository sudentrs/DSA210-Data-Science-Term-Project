# A Look into My Spending Habits
_This is my project for Sabanci University DSA210 Introduction to Data Science course Fall 2024-2025_
_The project website can be found **[here](https://sudentrs.github.io/)**_

## Description
The project consists of analyzing my personal bank transaction history data, particularly expenses. In the second part, I incorporate my daily emotional state to see how my emotions affect the purchases that I make.

## Table of Contents
**[Motivation](#motivation)**  

**[Data Source](#data-source)** 

**[Data Processing](#data-processing)**

**[Data Visualization](#data-visualization)**

**[Hypothesis Testing](#hypothesis-testing)**

**[Machine Learning](#machine-learning)**

**[Limitations and Future Work](#limitations-and-future-work)**

## Motivation
As a twenty-something-year-old living in Turkey in the current economic environment, I think it is safe to say that I have no idea how much I spend -or to be precise- I do not know how much of these purchases are justifiable. As the prices fluctuate, I can no longer confidently say that something deserves the price that says on the price tag. At the end of the day, I cannot help but feel like I have overspent. 

My aim in doing this project was to gain a deeper understanding of my spending habits through an analysis of my data and to see if I have any behavioural patterns that lead to overspending or tend to splurge in certain categories.

## Data Source
I have two main datasets
* My personal bank transaction history starts at the end of 2022.
* My daily emotional logs which are derived from my journal starting from 2023.

I got my transaction history from Akbank which is the main bank that  I use. Data was in an Excel file with columns representing time, date, transaction amount, balance, and description -which provides information about the content of my purchase. 

I have been keeping a journal in a physical format since the start of 2023. There are short entries for every day with occasional days that I forgot to write. To use this data for my project, I created an Excel file with columns date and mood. Depending on the general vibe and the content of the entry, I marked the mood for the day as strong negative, negative, mildly negative, neutral, mildly positive, positive, strong positive or no-entry.


## Data Processing
* ### Bank Transaction Dataset

Transaction history starts on 04.10.2022 and ends on 25.10.2022. The initial columns are "date, time, amount, balance, description, receipt number". The receipt number is not necessary for analysis so I deleted the column. 

I added a category column and wrote a Python code that gives unique descriptions and asks me for a category for each unique description. Code can be found in `pre_processing_bank_info.ipynb`. My initial categories were:
* *food*: descriptions that contain the words Getir, Trendyol Yemek, Yemeksepeti, Starbucks, and such. These purchases are made solely to fulfill my hunger-related needs.
* *clothing*: any purchase made from a clothing store or a secondhand store.
* *skincare/make-up*: purchases made from stores that sell skincare/make-up-related things. These purchases can contain shampoo, sunscreen, serums, lip balms etc.
* *social*: cinemas, museums, concerts and dining at cafes -I considered adding this to the food category but decided to go to a cafe and eating//drinking something is more fitted to social activity because it is almost all the time not done solely because of hunger but planned as an activity to do with friends- 
* *market*: descriptions that contain the names of market chains. It is impossible to keep track of what I bought at the time to give a more specific label like food. I also stay at the dormitories and most of my market purchases are from Şok market at school. None of the amounts in the market category is too high and there is a specific time and product range interval for the purchases, so it is unlikely that I find any out-of-the-ordinary/impulse purchases in this category.
* *other*: anything other than the above categories.

After the initial labelling, I created some count charts and decided that I labelled too many data lines as "other" so I added more categories:
* *thrifting*: Purchases I made at second-hand or vintage stores
* *education*: School payments and purchases made for course materials etc.
* *subscription*: Spotify, Netflix and such
* *transportation*: Istanbul kart, Kentkart and tickets purchased for transportation
* *travel cost*: Accommodation, plane tickets, visa cost and similar expenses that naturally occur when someone's travelling/on a holiday
* *credit card payment*: credit card paymnets were labelled seperately
* *investment*: money I invested into several things

Also, split skincare and make-up categories.


* ### Daily Emotional Log

After entering the daily emotional log entries into an Excel file, I combined my two datasets to create a final dataset that includes emotional state as a column in addition to bank transaction data. Related code can be found in `combine_datasets.ipynb` file.


## Data Visualization

Visualizations for both bank data and emotion data, also a combined analysis can be found in `EDA.ipynb` file. Note that not all graphs generated are used and because I used Plotly it cannot be seen on the GitHub environment for visualization results you should check the project **[website](https://sudentrs.github.io/)**


## Hypothesis Testing

My initial hypothesis was that some emotional states might be influencing my spending more than others. So I tested two cases for positive and negative states. Found out that some categories of purchases such as clothing or thrifting were more linked to positive mood than others. However, for negative moods, even though some categories have high negative rates, I failed to reject the null hypothesis which is there is nothing unusual about the category-negative mood relationship.


## Machine Learning

Firstly, I wanted to build a classification model to guess my emotional state according to the information given about my purchases. Which had a better accuracy than random guessing but was not satisfactory.

Then, I tried to build a model to classify data. Dropped some of the categories that had too few data points. The model had better results than the first one, when I tried to improve it further model bore the risk of overfitting. Categories like food have too many data points and there is not enough information about other categories, because of this food category overwhelms the model. Even though the results are good for most categories, there is not enough support for small categories.


## Limitations and Future Work

One of the main limitations that I faced was, that there were not enough data points for some of the categories which made it particularly hard to develop an ML model even when using cross-validation there was not enough support for categories. With a larger dataset across a longer period, the model could be improved. The other challenge was that my daily emotional log was in a physical format which was hard to digitalize. If it was in a digital format, I could have used sentiment analysis to label the data. Also while labelling the purchases I used the description column in the original data but due to the effect of time it was hard to recall or track down some of the purchases. I would also like to develop the website of the project further.
