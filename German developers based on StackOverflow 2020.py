#!/usr/bin/env python
# coding: utf-8

# ## German Developers based on StackOverflow 2020 Developers Survey
# 
# Scenario: A Competitor platform wants to know the results of 2020 developers survey based on German developers. The company needs detailed information from the survey to compare with their survey and see what developers like on a platform in order to make some decisions on how best to get developers to have an account on their own platform.
# 
# ### My task
# - Create a new dataframe for only German developers from the existing survey dataframe.
# - Analyzing this year's developer survey results to find interesting facts and directions in the software development community.
# - Percentage of German developers who took the survey.
# - Know developers who noticed a change in the StackOverflow platform.
# - What is the Age distribution?

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# ###  1 & 2 .  The survey results of the public dataset from stack Overflow for the year 2020.

# In[4]:


df=pd.read_csv(r'C:\Users\Uyoyo\Downloads\survey_results_public.csv')
df.head(2)


# In[5]:


df.columns


# In[6]:


df1=pd.read_csv(r'C:\Users\Uyoyo\Desktop\REDI SCHOOL HOMEWORK\FINAL PROJECT SPRING 2021\survey_results_schema.csv')
df1.head(2)

#df1[['QuestionText','Column']]


# In[7]:


df=df.replace(np.nan, 0)
df.head(2)


# ### Data filtering
# 
# ### Creating a new dataframe from existing survey data.
# 
# Specified country as Germany.

# In[8]:


df_dev_german=df[(df["MainBranch"] == "I am a developer by profession") & (df["Country"] == "Germany")].copy()
filter_german=df_dev_german
filter_german.head(1)


# In[9]:


filter_german.columns


# In[11]:


print(f' The number of German Developers by profession who took the StackOverflow survey is {filter_german.shape[0]}.')


# ### Removed Age=0

# In[12]:


df_dev_german=df[(df["MainBranch"] == "I am a developer by profession") & (df["Country"] == "Germany") & df["Age"] != 0].copy()
filtered_german=df_dev_german
filtered_german.head(1)


# ### Percentage of German developers who took the survey.

# In[13]:


print(f' The percentage of German developers who took the survey (inclusive of developers who did not provide their age) {round((len(filter_german)/len(df))*100,2)}%.')


# ### Developers who noticed a change on StackOverflow compared to last year
# 
# Question from the Survey - Compared to last year, how welcome do you feel on Stack Overflow?"
# 

# In[16]:


filter_change=filter_german[['MainBranch', 'Hobbyist', 'Age', 'Age1stCode', 'DatabaseDesireNextYear', 'DatabaseWorkedWith',
       'DevType', 'EdLevel', 'Employment', 'JobFactors',
       'JobSat', 'JobSeek', 'LanguageDesireNextYear', 'LanguageWorkedWith',
       'MiscTechDesireNextYear', 'MiscTechWorkedWith',
       'NEWCollabToolsDesireNextYear', 'NEWCollabToolsWorkedWith', 'NEWDevOps',
       'NEWJobHunt', 'NEWJobHuntResearch',
       'NEWLearn', 'NEWOffTopic', 'NEWOnboardGood', 'NEWOtherComms',
       'NEWOvertime', 'NEWPurchaseResearch', 'NEWPurpleLink', 'NEWSOSites',
       'NEWStuck', 'OpSys', 'OrgSize', 'PlatformDesireNextYear',
       'PlatformWorkedWith', 'PurchaseWhat', 'SOAccount',
       'SOComm', 'SOPartFreq', 'SOVisitFreq', 'UndergradMajor', 'WebframeDesireNextYear',
       'WebframeWorkedWith', 'WelcomeChange', 'WorkWeekHrs', 'YearsCode',
       'YearsCodePro']]
filter_change.head(1)


# In[17]:


filter_change.WelcomeChange.unique()


# In[18]:


from matplotlib.pyplot import figure
figure(figsize=(20,20), dpi=50)


filter_change.WelcomeChange.value_counts().plot(kind='pie',autopct='%1.1f%%',textprops={'fontsize': 20})


# In[11]:


filter_change.WelcomeChange.value_counts()


# Note that 11.5% did not provide an answer to the question or the data is missing. Information of 331 developers is not provided.
# 
# In the survey, 331 developers out of 2,877 German developers do not have an information about how they felt returning to StackOverflow.

# ### Concerning the Survey participation, what was their reaction to it

# In[13]:


filter_german.SurveyEase.value_counts()


# The number of German developers by profession from the given data had the opinion as follows:
# - 1785 developers chose "Easy".
# - 725 developers chose "Neither easy nor difficult"
# - 350 developers did not select or omitted answering the question (12.2%).
# - 17 found it difficult.

# In[19]:


from matplotlib.pyplot import figure
figure(figsize=(15,25), dpi=50)


filter_german.SurveyEase.value_counts().plot(kind='pie',autopct='%1.1f%%',textprops={'fontsize': 20})

#df['SurveyEase'].unique()


# ### Ploting the Age distribution

# #### Violin graph without filtering the Age which is zero

# In[20]:


#ax=sns.violinplot(x=filter_german['Age'], inner="box")
axx=sns.violinplot(y=filter_german['Age'], inner="box")


# #### Violin graph with filtered Age value != 0

# In[34]:


from matplotlib import pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))


ax1=sns.violinplot(x=filtered_german['MainBranch'],y=filtered_german['Age'], inner="box", width=0.8)


# In[36]:


from matplotlib import pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))

axee = sns.violinplot(data=filtered_german, x=filtered_german['MainBranch'], y=filtered_german['Age'], palette='turbo',
                    inner=None, linewidth=0, saturation=0.4)
sns.boxplot(x=filtered_german['MainBranch'], y=filtered_german['Age'], data=filtered_german, palette='turbo', width=0.3,
            boxprops={'zorder': 2}, ax=axee)


# In[37]:


print(f'The average age of German developers is {round(filtered_german.Age.mean())} years.')


# #### Would the age matter if the omitted or missing data was present?

# In[38]:


print(f' The percentage of developers who provided their age {round((1-(filter_german[filter_german.Age == 0].shape[0])/len(filter_german))*100,2)}%')


# In[39]:


print(f' The number of missing age in the survey is {filter_german[filter_german.Age == 0].shape[0]}.')


# In[40]:


print(f' The number of missing age in the survey is {(round((filter_german[filter_german.Age == 0].shape[0])/len(filter_german)*100,2))}%.')


# In[42]:


filter_german['Age'].value_counts(bins=12)


# #### Conclusion:
#     
# - If age is essential irrespective of 554 missing data then my suggestion would be targetting German developers in the age range of 20 to 45 years. 

# ### What is their Education level?

# In[43]:


#filter_german.EdLevel.nunique()
filter_german.EdLevel.unique()


# In[44]:


filter_german['Education']=filter_german['EdLevel'].map({'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)': 'Masters',
    'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)':'Secondary school',
    'Bachelor’s degree (B.A., B.S., B.Eng., etc.)':'Bachelors',
    'Professional degree (JD, MD, etc.)':'Professional degree',
    'Associate degree (A.A., A.S., etc.)': 'Associate degree',
    'Some college/university study without earning a degree':'Study but no degree',
    'Other doctoral degree (Ph.D., Ed.D., etc.)':'Doctoral degree',
    '0':0,
    'Primary/elementary school':'Elementary school',
    'I never completed any formal education':'Never Completed'})


# ### Number of German Developers with their education level

# In[46]:


filter_german.Education.value_counts()


# In[47]:


filter_german.Education.mode()


# In[48]:


#filter_german.Employment.nunique()
filter_german.Employment.unique()


# In[49]:


filter_german.SOAccount.unique()


# ### Data Acquisition
# 
# Convert string to number using JobSat.

# ### What drives a developer to look for a new job and how satisfied are the developers with their job?
# 

# In[63]:


filter_german.JobSat.unique()


# In[64]:


filter_german['JobSatNum']=filter_german['JobSat'].map({'Slightly satisfied':4, 'Very satisfied':5, 0:0, 'Slightly dissatisfied':2,
       'Very dissatisfied':1, 'Neither satisfied nor dissatisfied':3})
filter_german.head(2)


# In[65]:


print(f' There are {filter_german.NEWJobHunt.nunique()} reasons why a developer would hunt for a new job. This is much and is best to use another parameter.')


# In[66]:


employ_jobsat=filter_german[(['Employment','JobSatNum'])]
#employ_jobsat=employ_jobsat.query('JobSatNum'!=0)
employ_jobsat.head(2)


# In[67]:


employ_jobsat1=employ_jobsat[(employ_jobsat["Employment"] != 0) & (employ_jobsat["JobSatNum"] != 0)].copy()
employ_jobsat1.head()
employ_jobsat1.shape
print(f' The number of developers who provided their job satisfaction answers are {employ_jobsat1.shape[0]}.')


# In[68]:


employ_jobsat0=employ_jobsat[(employ_jobsat["Employment"] != 0) & (employ_jobsat["JobSatNum"] == 0)].copy()
employ_jobsat0.head()
employ_jobsat0.shape
print(f' The number of developers who did not provide their job satisfaction answers are {employ_jobsat0.shape[0]}.')


# In[69]:


sns.histplot(data=employ_jobsat1, y='Employment', x='JobSatNum')


# In[70]:


ax_employ = sns.violinplot(x="JobSatNum", y="Employment", data=employ_jobsat1)


# #### Conclusion
# 
# From the Violin plot, the following was gathered:
# - Employed full-time: In the survey, developers who are employed full time 

# In[71]:


job_satnum=filter_german[['JobSat','JobSatNum']]
job_satnum.head(2)


# In[73]:


employ_jobsat1.Employment.value_counts()


# In[74]:


employ_fulltime=employ_jobsat1[(employ_jobsat1['Employment']=='Employed full-time')]
employ_fulltime.value_counts()


# In[76]:


print(f' The developers who work full-time and are very satisfied with their job is 737 out of {len(employ_fulltime)}.')


# In[77]:


employ_indep=employ_jobsat1[(employ_jobsat1['Employment']=='Independent contractor, freelancer, or self-employed')]
employ_indep.value_counts()


# In[79]:


print(f' The developers who are either an independent contractor, freelancer, or self-employed and are very satisfied with their job is 98 out of {len(employ_indep)}.')


# In[80]:


employ_parttime=employ_jobsat1[(employ_jobsat1['Employment']=='Employed part-time')]
employ_parttime.value_counts()


# In[81]:


print(f' The percentage of Developers who work part-time and are slightly satisfied with their job is 67 out of {len(employ_parttime)}.')


# In[82]:


sns.jointplot(data=employ_jobsat1,y='Employment',x='JobSatNum')
#sns.barplot(data=employ_jobsat1,y='Employment',x='JobSatNum', hue='group')


# In[83]:


employ_jobsat1.plot.hist()


# In[84]:


employ_jobsat1.JobSatNum.unique()


# In[85]:


#sns.histplot(employ_jobsat, x='JobSatNum', y='Employment')

sns.barplot(
    x='JobSatNum',
    y='Employment',
    data=employ_jobsat1
)


# ###    How many survey participants are  "Developer (someone who codes)/not"  and how many are they in total?

# In[97]:


df_dev_german=df[(df["MainBranch"] == "I am a developer by profession") & (df["Country"] == "Germany")].copy()
data=df_dev_german
data.head(1)


# In[98]:


data.Country.unique()


# In[99]:


print(f' The number of German developer participants are {data.shape[0]}.')


# In[100]:


df_dev_german=df[(df["MainBranch"] == "I am a developer by profession") & (df["Country"] == "Germany") & df["DatabaseWorkedWith"] != 0].copy()
database=df_dev_german
database.head(1)


# In[101]:


database.shape


# In[102]:


print(f'The percentage of the German developers who gave details of the database worked with is {(round((len(database)/len(data)*100),2))}%.')


# ###      Three most popular Database worked with.
# 
# Filtered Database worked with. Missing data has been removed.

# In[103]:


database1=(database['DatabaseWorkedWith']).value_counts()
database1


# The DatabaseWorkedWith column has combined database in some of the entries. It is best to separate it.

# ####  In order to get the exact sum of each Database worked with; we expand the Database column as see below.

# ###   Expanding the columns for further understanding.

# In[104]:


def expand_column(df,col):
    "Expand a column with semicolon-separated-values into multiple boolean columns, one for each value in the original column."

    df = df.copy()

    if col not in df.columns:
        raise ValueError(f"Column {col} not found in DataFrame")

    values = set()
    for row in df[col]:
        if not pd.isna(row):
            for value in row.split(";"):
                values.add(value)

    for value in values:
        df[f"{col}_{value}"] = df[col].map(
            lambda v: value in v.split(";") if not pd.isna(v) else False
        )

    return df


# ### Expanding the column of DatabaseWorkedWith for German Developers

# In[108]:


#exp_Database= expand_column(filter_german,"DatabaseWorkedWith")
#exp_Database.head(2)

exp_Database= expand_column(data,"DatabaseWorkedWith")
exp_Database.head(2)


# ### Filtering the columns of the dataframe, to only contain columns from the expansion.

# In[253]:


exp_Database.columns


# ###   Filter the columns of the dataframe, to only contain columns from the expansion. 

# In[254]:


expand_DB = exp_Database[['DatabaseWorkedWith_SQLite',
       'DatabaseWorkedWith_Cassandra', 'DatabaseWorkedWith_DynamoDB',
       'DatabaseWorkedWith_MongoDB', 'DatabaseWorkedWith_Couchbase',
       'DatabaseWorkedWith_PostgreSQL', 'DatabaseWorkedWith_Elasticsearch',
       'DatabaseWorkedWith_Microsoft SQL Server', 'DatabaseWorkedWith_Redis',
       'DatabaseWorkedWith_Firebase', 'DatabaseWorkedWith_MariaDB',
       'DatabaseWorkedWith_MySQL', 'DatabaseWorkedWith_Oracle',
       'DatabaseWorkedWith_IBM DB2']]
expand_DB.head()


# ###   Sum and sort values of the database German developers work with

# In[255]:



expand_DB = expand_column(df, "DatabaseWorkedWith")
expand_DB [[
"DatabaseWorkedWith_PostgreSQL",
"DatabaseWorkedWith_MariaDB",
"DatabaseWorkedWith_IBM DB2",
"DatabaseWorkedWith_Cassandra",
"DatabaseWorkedWith_Microsoft SQL Server",
"DatabaseWorkedWith_Couchbase",
"DatabaseWorkedWith_Firebase",
"DatabaseWorkedWith_Elasticsearch",
"DatabaseWorkedWith_Redis",
"DatabaseWorkedWith_SQLite",
"DatabaseWorkedWith_MySQL",
"DatabaseWorkedWith_MongoDB",
"DatabaseWorkedWith_DynamoDB",
"DatabaseWorkedWith_Oracle",
]
].sum().sort_values(ascending=False)


# 
# #### Now we have correct numbers od database worked with and the three(3) most popular are:
# - MySQL.
# - PostgreSQl.
# - Microsoft SQL Server.

# ### The top 5 languages which  German developers work with.

# ####  9.1  Exapnding LanguageWorkedWith

# In[260]:


exp_lang=expand_column(data, "LanguageWorkedWith")
exp_lang.head(2)


# In[261]:


## I could properly see the expansion of the LanguageWorkedwith

exp_lang.columns


# ###    Dataframe with only expanded columns of LanguageWorkedwith.

# In[263]:


exp_lang=exp_lang[['LanguageWorkedWith_SQL',
       'LanguageWorkedWith_Java', 'LanguageWorkedWith_C',
       'LanguageWorkedWith_PHP', 'LanguageWorkedWith_Dart',
       'LanguageWorkedWith_Kotlin', 'LanguageWorkedWith_Swift',
       'LanguageWorkedWith_JavaScript', 'LanguageWorkedWith_Ruby',
       'LanguageWorkedWith_Go', 'LanguageWorkedWith_VBA',
       'LanguageWorkedWith_HTML/CSS', 'LanguageWorkedWith_Julia',
       'LanguageWorkedWith_C++', 'LanguageWorkedWith_Assembly',
       'LanguageWorkedWith_Python', 'LanguageWorkedWith_R',
       'LanguageWorkedWith_Rust', 'LanguageWorkedWith_Perl',
       'LanguageWorkedWith_Scala', 'LanguageWorkedWith_TypeScript',
       'LanguageWorkedWith_Bash/Shell/PowerShell',
       'LanguageWorkedWith_Haskell', 'LanguageWorkedWith_C#',
       'LanguageWorkedWith_Objective-C']]
exp_lang.head(2)


# ### Sum of the Languages worked with by developers.

# In[264]:


exp_lang[['LanguageWorkedWith_SQL',
       'LanguageWorkedWith_Java', 'LanguageWorkedWith_C',
       'LanguageWorkedWith_PHP', 'LanguageWorkedWith_Dart',
       'LanguageWorkedWith_Kotlin', 'LanguageWorkedWith_Swift',
       'LanguageWorkedWith_JavaScript', 'LanguageWorkedWith_Ruby',
       'LanguageWorkedWith_Go', 'LanguageWorkedWith_VBA',
       'LanguageWorkedWith_HTML/CSS', 'LanguageWorkedWith_Julia',
       'LanguageWorkedWith_C++', 'LanguageWorkedWith_Assembly',
       'LanguageWorkedWith_Python', 'LanguageWorkedWith_R',
       'LanguageWorkedWith_Rust', 'LanguageWorkedWith_Perl',
       'LanguageWorkedWith_Scala', 'LanguageWorkedWith_TypeScript',
       'LanguageWorkedWith_Bash/Shell/PowerShell',
       'LanguageWorkedWith_Haskell', 'LanguageWorkedWith_C#',
       'LanguageWorkedWith_Objective-C']].sum().sort_values(ascending=False)


# #### Conclusion:
# The top 5 languages German Developers work with:
# 1. JavaScript.
# 2. HTML/CSS.
# 3. SQL.
# 4. Java.
# 5. Python.

# ### "How important is a formal education, such as a university degree in computer science, to your career?

# In[265]:


data.columns


# In[267]:


data.NEWEdImpt.value_counts()


# ### Do you have a Stack Overflow account?
# 

# In[268]:


data.SOAccount.value_counts()


# ### Do you consider yourself a member of the Stack Overflow community?
# 

# In[269]:


data.SOComm.value_counts()


# ### How frequently do you learn a new language or framework?
# 

# In[270]:


data.NEWLearn.value_counts()


# ### How frequently would you say you visit Stack Overflow?
# 

# In[271]:


data.SOVisitFreq.value_counts()


# ### WebframeDesireNextYear,"Which web frameworks have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the framework and want to continue to do so, please check both boxes in that row.)"
# 

# In[272]:


#data.WebframeDesireNextYear.value_counts().head(10)        # the top 10 webframes desired for next year
data.WebframeDesireNextYear.value_counts()


# In[273]:


data.WebframeDesireNextYear.mode()


# In[274]:


exp_webframe= expand_column(data,"WebframeDesireNextYear")
exp_webframe.head(2)


# In[275]:


exp_webframe.columns


# In[276]:


exp_webframe[['WebframeDesireNextYear_Symfony',
       'WebframeDesireNextYear_ASP.NET Core', 'WebframeDesireNextYear_Django',
       'WebframeDesireNextYear_ASP.NET', 'WebframeDesireNextYear_React.js',
       'WebframeDesireNextYear_Vue.js', 'WebframeDesireNextYear_Express',
       'WebframeDesireNextYear_Angular.js',
       'WebframeDesireNextYear_Ruby on Rails', 'WebframeDesireNextYear_Flask',
       'WebframeDesireNextYear_Angular', 'WebframeDesireNextYear_jQuery',
       'WebframeDesireNextYear_Laravel', 'WebframeDesireNextYear_Gatsby',
       'WebframeDesireNextYear_Spring', 'WebframeDesireNextYear_Drupal']].sum().sort_values(ascending=False)


# #### Conclusion:
#     
# The top 5 webframes desired to work with:
# 1. React.js
# 2. Vue.js
# 3. Angular
# 4. Spring
# 5. ASP.NET Core

# ### "Which platforms have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the platform and want to continue to do so, please check both boxes in that row.)"
# 

# In[278]:


data.PlatformDesireNextYear.value_counts()


# In[280]:


exp_platform= expand_column(data,"PlatformDesireNextYear")
exp_platform.head(1)


# In[281]:


exp_platform.columns


# In[282]:


exp_platform[['PlatformDesireNextYear_Linux',
       'PlatformDesireNextYear_WordPress', 'PlatformDesireNextYear_iOS',
       'PlatformDesireNextYear_Android', 'PlatformDesireNextYear_AWS',
       'PlatformDesireNextYear_MacOS', 'PlatformDesireNextYear_Raspberry Pi',
       'PlatformDesireNextYear_Google Cloud Platform',
       'PlatformDesireNextYear_Windows',
       'PlatformDesireNextYear_Microsoft Azure',
       'PlatformDesireNextYear_Heroku', 'PlatformDesireNextYear_Arduino',
       'PlatformDesireNextYear_Slack Apps and Integrations',
       'PlatformDesireNextYear_Docker',
       'PlatformDesireNextYear_IBM Cloud or Watson',
       'PlatformDesireNextYear_Kubernetes']].sum().sort_values(ascending=False)


# #### Conclusion:
#     
# The top 10 platforms desired to work with next year:
# 1. Linux 
# 2. Docker 
# 3. Windows
# 4. Kubernetes
# 5. Raspberry Pi
# 6. AWS
# 7. Android
# 8. MacOS 
# 9. Microsoft Azure 
# 10. Google Cloud Platform

# In[ ]:




