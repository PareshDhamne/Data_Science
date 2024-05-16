# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:32:47 2023

@author: PARESH DHAMNE
"""

import pandas as pd
anime=pd.read_csv("D:/8-RECOMMENDATION SYSTEM/anime.csv",encoding='utf-8')
anime.shape
#you will get 12294,7 matrix
anime.columns
anime.genre
#hee we are considering only genre
from sklearn.feature_extraction.text import TfidfVectorizer
#this is term frequency inverse document
#each row is treated as document
tfidf=TfidfVectorizer(stop_words='english')
#it is going to create tfidvectorizer to separate all stop words
#it is going to separate
#not all rows from the row
#now let us check is there any null values
anime['genre'].isnull().sum()
#there are 62 null values
#suppose only movie has got genre drama,Romance
#there may be many empty space
#so let us impute these empty spaces general is like simple imputer
anime['genre']=anime['genre'].fillna('general')
#now let us create tfidf_matrix
tfidf_matrix=tfidf.fit_transform(anime.genre)
tfidf_matrix.shape
#you will get 12294,47 matrix
#it has created sparse matrix it means
#that we ahave 47 genre on this perticular matrix
#we want to do item base recommendation if a user has
#watched gather then you can recommend shershah movie
from sklearn.metrics.pairwise import linear_kernel
#this is for measuring similarity
cosine_sim_matrix=linear_kernel(tfidf_matrix,tfidf_matrix)
#each elemetn of tfidf_matrix is comapred
#with each element of tfidf_matrix only
#output will be similarity marix of size 122----- size
#here is cosine_sim_matrix,
#there are no movie names only index are provided
#we will try to map movie name with movie index given
#for that purpose custom function function is written
anime_index=pd.Series(anime.index,index=anime['name']).drop_duplicates()
#we are converting anime_index series format, we want index and corresponding matrix
anime_id=anime_index['Assassins (1995)']
anime_id

def get_recommendations(name,topN):
    #topN=10
    #name=Assassins (1995)
    anime_id=anime_index[name]
    
    #we want to capture whole row of given movie
    #name, its score and column id
    #fro that purpose we are applyong cosine_sim_matrix to enumrate function
    #enumrate function create an object
    #which we need to create in a list form
    #we are using enumrate fucntion
    #wghat enumrate does suppose we have given 
    #(2,10,15,18),if we apply to enumrate then it will create a list
    #[0,2 1,10  3,15  4,18]
    cosine_scores=list(enumerate(cosine_sim_matrix[anime_id]))    
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
    cosine_scores_N=cosine_scores[0: topN+1]
    #Geetting the movie index
    anime_idx=[i[0] for i in cosine_scores_N]
    #getting cosine scores
    anime_scores=[i[1] for i in cosine_scores_N]
    #we are going to use this information to create a dataframe
    #create a empty dataframe
    anime_similar_show=pd.DataFrame(columns=['name','score'])
    #assign anime_idx to name column
    anime_similar_show['name']=anime.loc[anime_idx,'name']
    #assign score to score column
    anime_similar_show['score']=anime_scores
    #while assigning values it is by default capturing orignal index
    #we wan ttor create the index
    anime_similar_show.reset_index(inplace=True)
    print(anime_similar_show)
#enter your anime and number of anime to be recommended
get_recommendations('Bad Boys (1995)',topN=10)
