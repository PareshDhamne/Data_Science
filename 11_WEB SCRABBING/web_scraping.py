# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:21:21 2023

@author: Hp
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(open("D:/WEB SCRABBING/sample_doc.html"),'html.parser')
print(soup)
#it is going to show all the html contents extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table

for row in soup.find_all('tr'):
    for col in soup.find_all('td'):
        print(col)
        print(row)

for row in soup.find_all('tr'):
    columns=row.find_all('td')
    print(columns)