#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


#Load the dataset into the Dataframework

netflix_data = pd.read_csv(r"C:\Users\Ogbemudia\Music\OneDrive\Desktop\netflix_titles.csv")


# In[17]:


import os
print(os.getcwd())


# In[42]:


Netflix_shows_movies = netflix_data.copy()
Netflix_shows_movies


# In[47]:


Netflix_shows_movies.describe()


# In[48]:


Netflix_shows_movies.info()


# In[53]:


Netflix_shows_movies.isnull().sum()


# In[68]:


Netflix_shows_movies.fillna(value={'director': 'Unknown', 'cast': 'Unknown', 'country': 'Unknown', 'date_added': 'Unknown', 'rating': 'Unknown'}, inplace=True)


# In[69]:


Netflix_shows_movies.isnull().sum()


# In[75]:


Netflix_shows_movies['type'].value_counts()


# In[80]:


Netflix_shows_movies['country'].value_counts()


# In[81]:


import seaborn as sns
import matplotlib.pyplot as plt

# Most watched genres
plt.figure(figsize=(12, 6))
sns.countplot(y='listed_in', data=netflix_data, order=netflix_data['listed_in'].value_counts().index[:10])
plt.title('Top 10 Most Watched Genres on Netflix')
plt.xlabel('Number of Shows/Movies')
plt.ylabel('Genre')
plt.show()

# Ratings distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='rating', data=netflix_data, order=netflix_data['rating'].value_counts().index)
plt.title('Ratings Distribution on Netflix')
plt.xlabel('Rating')
plt.ylabel('Number of Shows/Movies')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




