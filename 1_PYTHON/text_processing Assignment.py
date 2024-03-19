# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:00:29 2023

@author: Hp
"""
from PyPDF2 import PdfFileReader
#import required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader = PdfReader("D:/PARESH1_python/Iot Report.pdf")

#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page = reader.pages[10]

#extracting text from page
text=page.extract_text()
text
#################################################

import re
a='Hi: I have a problem with my older number 4124334'
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern,a)
print(matches)

################################################
import re
text1="My mobile number is 9665779167"
text2="my other mobile number is 82751196357"
text3="My international mobile number is (124)-456-75432"
pattern='\d{10}'
mob_num=re.findall(pattern,text1)
mob_num
#if we write /d 10 times it will be show 10 numbers but insted of
#lengthy method we use simply \d{10}
patt2='\(\d{3}\)\-\d{3}-\d{5}'#to get pattern between parenthesis use ]\()
mob=re.findall(patt2,text3)
mob
#############################################

#matching emailid
text1="My-email-id  is pareshdhamane19@gmail.com"
text2="My alternate emailid is princedhamane02@gmail.com"
patt="[a-zA-z0-9]*@[a-z]*\.*com"
a=re.findall(patt,text1)
a
text3="My college mail id is paresh.dhamne@sanjivani.org.in"
patt="[a-zA-Z]*\.*[a-z]*@*[a-z]*\.*org*\.*in"
a=re.findall(patt,text3)
a
##################################################3
chat1="Hi my order #59326 is not received yet"
chat2="Hi I have problem with my order number 59326, which is not received"
chat3="Hi my order 59326 is having an issue"
patt='order[^\d]*(\d*)'
b=re.findall(patt,chat1)
b
c=re.findall(patt,chat2)
c
d=re.findall(patt,chat3)
d
############################################

def get_pattern_match(pattern,text):
    matches= re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)   
############################################

#retrive email id and phone
chat1='Hi: you ask lot of questions 9665779167, pareshdhamane19@gmail.com'
chat2=
#####################################
###############################################
text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and chairman of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp. and X.AI
Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[a][3]
Parents	
Errol Musk (father)
Maye Musk (mother)
Family	Musk family
'''
get_pattern_match('age (\d*)', text) #or we can give 'age (\d+)'
############################################
get_pattern_match(r'Born(.*)',text)
match[0].strip()
get_pattern_match(r'Born(.*)',text).lstrip()
###########################################
get_pattern_match(r'Born.*\n(.*)\(age',text)
get_pattern_match(r'\(age.*\n(.*)',text)
########################################

def extract_data(text):
    age=get_pattern_match(r'age (\d*)', text)
    name=get_pattern_match(r'Born(.*)', text)
    birth_date=get_pattern_match(r'Born.\n(.)\(age', text)#It will give only the date
    birth_place=get_pattern_match(r'\(age.\n(.)', text)#It will give birthplace
    return{
        'age':age,
        'name':name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_data(text)
##########################################

text='''Born   Mukesh Dhirubhai Ambani
19 April 1957 (age 66 years), 
Aden, Yemen
Net worth: 8,860 crores USD (2023) Forbes
Children: Akash Ambani, Anant Ambani, Isha Ambani
Spouse: Nita Ambani (m. 1985)
Siblings: Anil Ambani, Nina Kothari, Deepti Salgaocar
Parents: Dhirubhai Ambani, Kokilaben Ambani
Education: Institute of Chemical Technology (ICT), St. Xavier's College (Autonomous), Hill Grange High School, Forest School
'''
#for age display
get_pattern_match('age (\d*)', text)
#############################################
#for name Display
get_pattern_match(r'Born(.*)',text)
get_pattern_match(r'Born(.*)',text).lstrip()
#########################################
#for birth date and birth place
get_pattern_match(r'Born.*\n(.*)\(age',text)
get_pattern_match(r'\(age.*\n(.*)',text)
######################################
def extract_data(text):
    age=get_pattern_match(r'age (\d*)', text)
    name=get_pattern_match(r'Born(.*)',text).lstrip()
    birth_date=get_pattern_match(r'Born.\n(.)\(age', text)#It will give only the date
    birth_place=get_pattern_match(r'\(age.\n(.)', text)#It will give birthplace
    return{
        'age':age,
        'name':name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_data(text)
#############################################

#1. Extract all twitter handles from following text. Twitter handle is the
text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern='https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
##########################################
#2. Extract 
text='''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31,
'''
pattern='Concentration of Risk: ([^\n]*)'
re.findall(pattern,text)
#################################################
#companies in europe reports their financial numbers od semi annual basics
#and you can have documnent 

text='''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))' #match this
matches=re.findall(pattern,text)
matches
##################################

#EXTRACT PHONE NUMBERS
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches
##################################

text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern, text)
matches
##########################################

#
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text)
matches
#########################################
#Case insensitive  pattern match using flags
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern, text, flags=re.IGNORECASE)
matches

#################################################
#extract only financial numbers
text='''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='\$([0-9\.]+)'
matches=re.findall(pattern,text)
matches
###############################################
