# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:09:24 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    The Entertainment Company, which is an online movie watching platform, wants to improve its 
    collection of movies and showcase those that are highly rated and recommend those movies to 
    its customer by their movie watching footprint. For this, the company has collected the data 
    and shared it with you to provide some analytical insights and also to come up with a recommendation 
    algorithm so that it can automate its process for effective recommendations. The ratings are between 
    -9 and +9.

Business Problem:
    1.1.	What is the business objective?
    - Maximize:Maximize the overall engagement of users on the platform.
    - Minimize:Minimize the operational costs associated with acquiring new content that might not be popular.
    -constraints:Ensure that user data is handled with privacy in mind, complying with regulations and user expectations.
    
    
DATA DICTIONARY:
    
    Id          ordinal data   Id is unique id related to the title of the movie
    Titles      nominal data   title represents the name of movie for recomeendation
    Category    ordinal data   Category represents in which category movie belongs
    Reviews     ordinal data   Review represents the review related to the movie
"""
import pandas as pd
import seaborn as sns
movie=pd.read_csv("D:/8-RECOMMENDATION SYSTEM/Entertainment.csv",encoding='utf-8')
movie

#####################################

#EDA

movie.columns
#Index(['Id', 'Titles', 'Category', 'Reviews'], dtype='object')
#####################################################

movie.dtypes

'''
Id            int64
Titles       object
Category     object
Reviews     float64
dtype: object

Id and Reviews are numerical data while remeaning are object data
'''
######################################################

movie.describe()
#It will dispaLAY 5 no summary
#standard deviation is showing diffrence with mean
# so the datapoints are scatter from median

######################################################

movie.shape
#(51, 4) matrix shape
##########################################

movie.Category
#we are considering only Category column for recommendation
#####################################################

# Outlier Analysis

# Plot the boxplot to identify whether the dataset contain any oulier or not

sns.boxplot(movie['Id'])
# The data is normally distributed as the data not contain the outlier and he central tendancy also it shows

sns.boxplot(movie['Reviews'])
# The data is normally distributed as the data not contain the outlier and he central tendancy also it shows

#Plot the pairplot and heatmap to understand the relationship between the columns

sns.pairplot(movie)
# The data is more scatter 
##########################################################

#Model Building

from sklearn.feature_extraction.text import TfidfVectorizer
#this is term frequency inverse document
#each row is treated as document
tfidf=TfidfVectorizer(stop_words='english')
#it is going to create tfidvectorizer to separate all stop words
#it is going to separate
#not all rows from the row
#now let us check is there any null values
movie['Category'].isnull().sum()
#there is no null value present in it
########################################################

#let us impute these empty spaces general is like simple imputer
movie['Category'] = movie['Category'].fillna('general')
#now let us create tfidf_matrix
tfidf_matrix=tfidf.fit_transform(movie.Category)
# it has created sparse matrix
tfidf_matrix.shape
 #(51, 34)
#we will get 51,34 matrix
#it has created sparse matrix it means
#that we ahave 34 game on this perticular matrix
#we want to do item base recommendation

######################################################

from sklearn.metrics.pairwise import linear_kernel
#this is for measuring similarity
cosine_sim_matrix=linear_kernel(tfidf_matrix,tfidf_matrix)
#each elemetn of tfidf_matrix is comapred
#with each element of tfidf_matrix only
#output will be similarity marix
#here is cosine_sim_matrix,
#there are no movie names only index are provided
#we will try to map movie name with movie index given
#for that purpose custom function function is written
movie_index = pd.Series(movie.index, index=movie['Titles']).drop_duplicates()
#we are converting movie_index series format, we want index and corresponding matrix
movie_id=movie_index['Father of the Bride Part II (1995)']
movie_id
#####################################################

def get_recommendations(Titles,topN):
    #topN=10
    movie_id=movie_index[Titles]
    
    cosine_scores=list(enumerate(cosine_sim_matrix[movie_id]))    
    #the cosine scores captured we want arraange in decending order
    #in that we can recomment top 10 based on highest similarity I.e. score
    #ir will check the column score it comprises of indexcosine score
    #x[0]=index and x[1] is cosine scord\e
    #we want arrange tuples according to decreasing order
    #of the score not index
    #sorting the cosine_similarity scores based on scores i.e. x[1]
    cosine_scores=sorted(cosine_scores, key=lambda x:x[1], reverse=True)
    #get the scores of top n most similar movie
    #to capture TopN movies you need to give topN+1
    cosine_scores_N=cosine_scores[0:topN+1]
    #Geetting the movie index
    movie_idx=[i[0] for i in cosine_scores_N]
    #getting cosine scores
    movie_scores=[i[1] for i in cosine_scores_N]
    #we are going to use this information to create a dataframe
    #create a empty dataframe
    movie_similar_show=pd.DataFrame(columns=['Titles','score'])
    #assign movie_idx to name column
    movie_similar_show['Titles']=movie.loc[movie_idx,'Titles']
    #assign score to score column
    movie_similar_show['score']=movie_scores
    #while assigning values it is by default capturing orignal index
    #we want to create the index
    movie_similar_show.reset_index(inplace=True)
    print(movie_similar_show)
    
#############################################################

#enter your movie and number of movie to be recommended
get_recommendations('Father of the Bride Part II (1995)',topN=10)
#############################################################

'''
Benifits to the client:
    This recommendation algorithm boosts user engagement and satisfaction by suggesting tailored movies,
    while also optimizing content acquisition to minimize costs and comply with privacy regulations.
'''
#####################################################################
