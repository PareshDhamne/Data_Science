# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:39:30 2023

@author: Paresh Dhamne
"""

from bs4 import BeautifulSoup as bs
import requests
link='https://www.flipkart.com/canon-eos-m50-mark-ii-mirrorless-camera-ef-m15-45mm-stm-lens/p/itm7a4f536cb1255?pid=DLLGFY7XYG8YFMQT&lid=LSTDLLGFY7XYG8YFMQTSG43XC&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=dd234517-bb0d-475e-85a3-bac233080b4a.DLLGFY7XYG8YFMQT.SEARCH&ppt=hp&ppn=homepage&ssid=voe3titvkw0000001701747037542'
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
title=soup.find_all('p',class_="_2-N8zT")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)

#we got 3 revie wtitle
#now let us scrap rating
##################################################################

rating=soup.find_all('div',class_="_3LWZlK _1BLPMq")
rating

rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.append('')
rate.append('')
rate.append('')
len(rate)
###############################

review=soup.find_all('div',class_='t-ZTKy')
review

review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
#we got 10 review body
#now we have to save the data in ,csv file
######################################

import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['rate']=rating
df['Review_body']=review_body
df

#to create csv
df.to_csv("D:/WEB SCRABBING/flipkart_reviews.csv",index='True')
################################

#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is bad product"
pol=TextBlob(sent).sentiment.polarity
pol

df=pd.read_csv("D:/WEB SCRABBING/flipkart_reviews.csv")
df.head()
df['polarity']=df['Review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
