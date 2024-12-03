# A Look into My Spending Habits
_This is my project for Sabanci University DSA210 Introduction to Data Science course Fall 2024-2025_
_An initial template of the project website can be found **[here](https://sudentrs.github.io/)**_

## Description
The project consists of an analysis of my personal bank transaction history data -particularly expenses. In the second part of the project, I incorporate my daily emotional state to see how my emotions affect the purchases that I make.

## Table of Contents
**[Motivation](#motivation)**  

**[Data Source](#data-source)** 

**[My Plan](#my-plan)**

**[Data Processing](#data-processing)**

**[Data Visualization](#data-visualization)**

## Motivation
As a twenty-something-year-old living in Turkey in the current economic environment, I think it is safe to say that I have no idea how much I spend -or to be precise- I do not know how much of these purchases are justifiable. As the prices fluctuate, I can no longer confidently say that something deserves the price that says on the price tag. At the end of the day, I cannot help but feel like I have overspent. 

My aim in doing this project was to gain a deeper understanding of my spending habits through an analysis of my data and to see if I have any behavioural patterns that lead to overspending or tend to splurge in certain categories.

## Data Source
I have two main datasets
* My personal bank transaction history starting from the end of 2022.
* My daily emotional logs which are derived from my journal starting from 2023.

I got my transaction history from Akbank which is the main bank that  I use. Data was in an Excel file with columns representing time, date, transaction amount, balance, and description -which provides information about the content of my purchase. 

I have been keeping a journal in a physical format since the start of 2023. There are short entries for every day with occasional days that I forgot to write. To use this data for my project, I created an Excel file with columns date and mood. Depending on the general vibe and the content of the entry, I marked the mood for the day as strong negative, negative, mildly negative, neutral, mildly positive, positive, strong positive or no-entry.

## My Plan
After pre-processing datasets and explanatory data analysis, I hope to gain a better understanding of the datasets and come up with a better hypothesis but my initial guess is I do most of my impulse purchases during late hours and tend to spend more money when I am happy.

Firstly, I need to preprocess my bank information dataset because my focus is expenses and the dataset contains both money coming in and out of my account, also I need to categorize my purchases as food, clothing, education etc. The reason is the money I spend on education or subscriptions for example does not provide any information about my spending habits, these are things that are done out of schedule or out of necessity. The second step is to start visualising both datasets separately to familiarize myself with the data. Then I will start studying these datasets together to see if I can find any correlations and test my hypothesis. In the final stage, I would like to implement an ML model.


## Data Processing
* ### Bank Transaction Dataset

Transaction history starts on 04.10.2022 and ends on 25.10.2022. The initial columns are "date, time, amount, balance, description, receipt number". The receipt number is not necessary for analysis so I deleted the column. 

I added a category column and wrote a Python code that gives unique descriptions and asks me for a category for each unique description. Code can be found in `pre_processing.ipynb`. My initial categories were:
* *food*: descriptions that contain words Getir, Trendyol Yemek, Yemeksepeti, Starbucks and such. These are purchases that are made solely for the sake of fulfilling my needs related to hunger.
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
* *travel cost*: Accommodation, plane tickets, visa cost and and similar expenses that naturally occur when someone's travelling/on a holiday

Also, split skincare and make-up categories.





* ### Daily Emotional Log










## Data Visualization
_to be added_
