#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('StudentsPerformance.csv')


# In[5]:


df.describe()


# In[38]:


df.head()


# In[8]:


df.drop([ 'lunch','test preparation course'], axis =1,inplace = True)
df.head()


# In[9]:


df['parental level of education']= df['parental level of education'].fillna('X')


# In[10]:


df.head()


# In[11]:


df['race/ethnicity'] = df['race/ethnicity'].map({
    'group A': 'Asian Students',
    'group B': 'African Students',
    'group C': 'Afro-Asian Students',
    'group D': 'American Students',
    'group E': 'European Students'
    
})


# In[12]:


df.head(10)


# ## Data Visualization

# In[15]:


df = pd.read_csv('StudentsPerformance.csv')
import seaborn as sns


# In[19]:


ax = sns.countplot(x='gender', hue = 'test preparation course', palette ='Set1', data = df)
ax.set(title = "Gender wise course completion statistics",xlabel = 'Gender', ylabel = 'Number')
plt.show()


# In[25]:


df['race/ethnicity'] = df['race/ethnicity'].map({
    'group A': 'Asian Students',
    'group B': 'African Students',
    'group C': 'Afro-Asian Students',
    'group D': 'American Students',
    'group E': 'European Students'
    
})
ax = sns.countplot(x='parental level of education', hue = 'gender', palette ='Set1', data = df)
ax.set(title = "Gender wise student groups",xlabel = 'Level of education', ylabel = 'Number')
plt.figure(figsize=(500,500))
plt.show()


# In[28]:


interval = (0,40,50,75,120)
categories = ['Failed', 'Second Class', 'First Class', 'Distinction']
df['maths_cat'] = pd.cut(df['mathscore'],interval,labels = categories)
df['read_cat'] = pd.cut(df['reading score'],interval,labels = categories)
df['write_cat'] = pd.cut(df['writing score'],interval,labels = categories)


# In[30]:


ax = sns.countplot(x='maths_cat',palette ='Set3', data = df)
ax.set(title = "Categorical Distribution of Students for Maths Score",xlabel = 'Classes of distinction', ylabel = 'Number')
plt.show()


# In[37]:


ax = sns.countplot(x='write_cat',palette ='Set1', data = df)
ax.set(title = "Categorical Distribution of Students for Writing Score",xlabel = 'Classes of distinction', ylabel = 'Number')
plt.show()


# In[36]:


ax = sns.countplot(x='read_cat',palette ='Set2', data = df)
ax.set(title = "Categorical Distribution of Students for Reading Score",xlabel = 'Classes of distinction', ylabel = 'Number')
plt.show()


# In[ ]:



