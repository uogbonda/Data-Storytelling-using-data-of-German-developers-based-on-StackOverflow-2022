# Data-Storytelling-using-data-of-German-developers-based-on-StackOverflow-2022

## German Developers based on StackOverflow 2020 Developers Survey
Scenario: A Competitor platform (ADMAC) wants to know the results of 2020 developers survey based on German developers. The company needs detailed information from the survey to compare with their survey and see what developers like on a platform in order to make some decisions on how best to get developers to have an account on their own platform.


## Table of Content
* [General info](#general-info)
* [Technologies](#technologies)
* [German_Developers](#german_developers)
* [Data_Visualization](#data_visualization)


## General info
Get information from the data set:

- Create a new dataframe for only German developers from the existing survey dataframe.
- Analyzing this year's developer survey results to find interesting facts and directions in the software development community.
- Percentage of German developers who took the survey.
- Know developers who noticed a change in the StackOverflow platform.
- What is the Age distribution?

### General information on the survey
- The total number of people that took the survey were 83,439.
- In terms of employment; people were emploed full_time, have Student full_time jobs. Although other employment status options were in the survey.
- The first time they coded were mostly at age between "11-17" years mostly; followed by "18-24" years, "5-10" years.



## Technologies
Project performed on:
* Jupyter Notebook.
* Python version: 3.8.8

The following are Python libraries used:
- Pandas
- Seaborn
- Matplotlib


## German Developers

There were **83,439 participants** in the survey. Out of the 83,439 participants, **2877 (4.46%) were Germans**. The analysis was based on age, job satisfaction, database, language etc. Some of the developers did not give their opinion of some of the information needed. From the questions of the survey, we use it to give more details.

### German Developers Report

2877 German based developers took the survey. Specifically, analysizing "German developers by profession".

#### How welcomed the German Developers felt on Stack Overflow compared to last year?
The **missing data for this is 331** which is 11.5%. The following are the answers obtained from the survey:
![](German%20dev%20Stachflow/feelonstackflow.png)
- Just as welcome now as I felt last year were 2005.
- Somewhat less welcome now than last year were 187.
- Somewhat more welcome now than last year were 145.
- A lot less welcome now than last year were 98.
- Not applicable - I did not use Stack Overflow last year were 68.
- A lot more welcome now than last year were 43.

#### Reactions concerning the survey 
The number of German developers by profession from the given data had the opinion as follows:
 ![](German%20dev%20Stachflow/particatesurvey.png)
- 1785 developers chose "Easy".
- 725 developers chose "Neither easy nor difficult"
- 350 developers did not select or omitted answering the question (12.2%).
- 17 found it difficult.



#### The age distribution of the developers
The **average age of German developers is 32 years** and the percentage of developers who provided their age is **80.74%**. The number of missing age in the survey is **19.26%**.
The age data visualization is below:

![](German%20dev%20Stachflow/agedist.png)

**Conclusion**:
If age is essential irrespective of 554 missing data then my suggestion would be targetting German developers in the age range of 20 to 45 years.

#### What is their Educational level?
The Developers have the following educational level:
- 965 have Masters degree.
- 840 have Bachelors degree.
- 311 have studied but no degree.
- 308 have Secondary school certifcate.
- 110 have Doctoral degree.
- 80 have Associate degree.
- 40 have Professional degree.
- 6 never completed education.
- 5 have Elementary school certificate.

#### How important is a formal education, such as a university degree in computer science, to your career?
- 750 responded that is fairly important.
- 677 responded that is somewhat important.                    
- 600 responded that is very important.
- 412 responded that is not at all important/not necessary.   
- 181 responded that is critically important.                  

#### What is their employment status and how satisfied are the developers with their job?
The information gathered from the dataframe of employment and job satisfaction, most provided an answer. The number of developers who provided their job satisfaction answers are 2572 while 298 did not provide an answer.

Data acquisition was performed. Converting strings to numbers. The job satisfaction was coverting into the following:
Very satisfied - 5.
Slightly satisfied - 4.
Neither satisfied nor dissatisfied - 3.
Slightly dissatisfied - 2.
Very dissatisfied - 1.

![](German%20dev%20Stachflow/employjob.png)

Taking out the missing information on job satisfaction, there is only 3 employment status who provided their job satisfaction:
- 2175 are Employed full-time.                                     
- 212 are Independent contractor, freelancer, or self-employed.     
- 185 are Employed part-time.  
                                    
 **Conclusion**:
 - The developers who work full-time and are very satisfied with their job is 737 out of 2175.
 - The developers who are either an independent contractor, freelancer, or self-employed and are very satisfied with their job is 98 out of 212.

#### Three most popular Database worked with.
Filtered Database worked with. Missing data has been removed. The percentage of the German developers who gave details of the database worked with is **79.46%**.
Now we have correct numbers od database worked with and the **three(3)** most popular are:
- MySQL.
- PostgreSQl.
- Microsoft SQL Server.

#### The top 5 languages which German developers work with.
The top 5 languages German Developers work with:
- JavaScript.
- HTML/CSS.
- SQL.
- Java.
- Python.

## Data_Visualization

![](Stackflow%20images/age.png)

![](Stackflow%20images/categories.png)

![](Stackflow%20images/first.png)

![](Stackflow%20images/status.png)









