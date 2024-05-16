# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:01:38 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    Build a recommender system with the given data using UBCF.
    This dataset is related to the video gaming industry and a survey was conducted to build a 
    recommendation engine so that the store can improve the sales of its gaming DVDs. 
    Snapshot of the dataset is given below. Build a Recommendation Engine and suggest top selling DVDs 
    to the store customers.


Business Problem:
    1.1.	What is the business objective?
    - Maximize:Maximize customer satisfaction by providing personalized and relevant recommendations. 
    - Minimize:Minimize customer churn by keeping customers satisfied through effective recommendations.
    -constraints:Ensure that customer data is handled in compliance with privacy regulations and ethical standards.
    
    
DATA DICTIONARY:
    
    userid   ordinal data   user id is unique id related to the game name
    game     nominal data   game represents the name of games for recomeendation
    rating   ordinal data   rating represents the rating given for the game
"""
import pandas as pd
import seaborn as sns
game=pd.read_csv("D:/8-RECOMMENDATION SYSTEM/game.csv",encoding='utf-8')
game

#####################################

#EDA

game.columns
#Index(['userId', 'game', 'rating'], dtype='object')
#####################################################

game.dtypes

'''
userId      int64
game       object
rating    float64
dtype: object

all datatpes are numerical containing float and int values
'''
######################################################

game.describe()
#It will dispaLAY 5 no summary
#standard deviation is showing diffrence with mean
# so the datapoints are scatter from median

######################################################

game.shape
#(5000, 3) matrix shape
##########################################

game.game
#we are considering only rating column for recommendation
#####################################################

# Outlier Analysis

# Plot the boxplot to identify whether the dataset contain any oulier or not

sns.boxplot(game['userId'])
# The data is normally distributed as the data not contain the outlier and he central tendancy also it shows

sns.boxplot(game['rating'])
# it contain two outliers we can normalize the data

# 2. Plot the pairplot and heatmap to understand the relationship between the columns

sns.pairplot(game)
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
game['game'].isnull().sum()
#there is no null value present in it
########################################################

#let us impute these empty spaces general is like simple imputer
game['game'] = game['game'].fillna('general')
#now let us create tfidf_matrix
tfidf_matrix=tfidf.fit_transform(game.game)
# it has created sparse matrix
tfidf_matrix.shape
(5000, 3068)
#we will get 5000,3068 matrix
#it has created sparse matrix it means
#that we ahave 3068 game on this perticular matrix
#we want to do item base recommendation

######################################################

from sklearn.metrics.pairwise import linear_kernel
#this is for measuring similarity

cosine_sim_matrix=linear_kernel(tfidf_matrix,tfidf_matrix)
#each elemetn of tfidf_matrix is comapred
#with each element of tfidf_matrix only
#output will be similarity marix
#here is cosine_sim_matrix,
#there are no game names only index are provided
#we will try to map game name with game index given
#for that purpose custom function function is written
game_index = pd.Series(game.index, index=game['game']).drop_duplicates()
#we are converting game_index series format, we want index and corresponding matrix
userid=game_index['Super Mario Galaxy 2']
userid
#####################################################

def get_recommendations(games,topN):
    #topN=10
    game_id=game_index[games]
    
    cosine_scores=list(enumerate(cosine_sim_matrix[game_id]))    
    #the cosine scores captured we want arraange in decending order
    #in that we can recomment top 10 based on highest similarity I.e. score
    #ir will check the column score it comprises of indexcosine score
    #x[0]=index and x[1] is cosine scord\e
    #we want arrange tuples according to decreasing order
    #of the score not index
    #sorting the cosine_similarity scores based on scores i.e. x[1]
    cosine_scores=sorted(cosine_scores, key=lambda x:x[1], reverse=True)
    #get the scores of top n most similar game
    #to capture TopN games you need to give topN+1
    cosine_scores_N=cosine_scores[0:topN+1]
    #Geetting the game index
    game_idx=[i[0] for i in cosine_scores_N]
    #getting cosine scores
    game_scores=[i[1] for i in cosine_scores_N]
    #we are going to use this information to create a dataframe
    #create a empty dataframe
    game_similar_show=pd.DataFrame(columns=['game','score'])
    #assign game_idx to name column
    game_similar_show['game']=game.loc[game_idx,'game']
    #assign score to score column
    game_similar_show['score']=game_scores
    #while assigning values it is by default capturing orignal index
    #we want to create the index
    game_similar_show.reset_index(inplace=True)
    print(game_similar_show)
    
###########################################################
#enter your game and number of game to be recommended
get_recommendations('Super Mario Galaxy 2',topN=10)

###########################################################

'''
Benifits to the client:
    This user-based collaborative filtering recommendation system suggests personalized top-selling DVDs
    to maximize customer satisfaction and minimize churn, all while adhering to privacy regulations and 
    ethical standards.
'''
################################################################