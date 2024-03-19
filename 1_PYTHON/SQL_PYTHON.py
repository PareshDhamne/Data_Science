# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:28:26 2023

@author: Hp
"""

import psycopg2 as pg2

#create a connection with postgresql
#'password" is whatever password you set

conn=pg2.connect(database='dvdrental',user='postgres',password='Root')

#Estabilish connection and start cursor to be ready to query
cur=conn.cursor()

#Pass in a PostgreSQL query as a string
cur.execute("SELECT * FROM payment")

#return single row 
cur.fetchone()

#return n number of records
cur.fetchmany(10)

#fetch all records
cur.fetchall()

#to save and index result, assign it to a variabe
data=cur.fetchmany(10)

#don't forget to close the connection
#killing the kernel
conn.close()

#create table
import psycopg2 as pg2

conn=pg2.connect(database='test_me',user='postgres',password='Root')

curr=conn.cursor()

curr.execute("""CREATE TABLE courses1(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) UNIQUE NOT NULL,
    course_instructor VARCHAR(100) NOT NULL,
    topic VARCHAR (20) NOT NULL);
""")

conn.commit()
curr.close()

#9 SEPT 2023

import psycopg2 as pg2

conn=pg2.connect(database='test_me',user='postgres',password='Root')

curr=conn.cursor()

curr.execute('''INSERT INTO courses1(course_name,course_instructor,topic) 
             VALUES ('Python','Ram','Theory')''');

curr.execute('''INSERT INTO courses1(course_name,course_instructor,topic) 
             VALUES ('Introduction to CHATGPT','Sham','Practical')''');
             
curr.execute('''INSERT INTO courses1(course_name,course_instructor,topic) 
                VALUES ('Introduction to SQL','Sam','Practical')'''); 
                
curr.execute('''INSERT INTO courses1(course_name,course_instructor,topic) 
             VALUES ('web develpoment','Sham','Basic')''');
conn.commit()
curr.close()
conn.close()

import psycopg2 as pg2

conn=pg2.connect(database='test_me',user='postgres',password='Root')

curr=conn.cursor()

curr.execute('SELECT * FROM courses1;')
rows=curr.fetchall()
conn.commit()
conn.close()

for row in rows:
    print(row)
################################ 
#GROUP BY
import psycopg2 as pg2
conn=pg2.connect(database='test_me',user='postgres',password='Root')
curr=conn.cursor()

curr.execute('''SELECT course_instructor,COUNT(*)
                FROM courses1 GROUP BY course_instructor
                ''')
conn.commit()
rows=curr.fetchall()
for row in rows:
    print(row)

############################
#ORDER BY
curr.execute('''SELECT * 
                FROM courses1 ORDER BY course_instructor
                ''')
conn.commit()
rows=curr.fetchall()
for row in rows:
    print(row)
conn.close()
    
####################################

#ASSIGNMENT
import psycopg2 as pg2
conn=pg2.connect(database='test_me',user='postgres',password='Root')
curr=conn.cursor()

curr.execute("""CREATE TABLE course_admin(
    course_id SERIAL PRIMARY KEY,
    course_duration VARCHAR(30) NOT NULL,
    course_fees INTEGER NOT NULL);
""")
conn.commit()

curr.execute('''INSERT INTO course_admin(course_duration,course_fees)
             VALUES
             ('3 months',30000);
             ''')
             
curr.execute('''INSERT INTO course_admin(course_duration,course_fees)
             VALUES
             ('30 days',2000);
             ''')
             
curr.execute('''INSERT INTO course_admin(course_duration,course_fees)
             VALUES
             ('2 months',20000);
             ''')

curr.execute('''INSERT INTO course_admin(course_duration,course_fees)
             VALUES
             ('12 months',30000);
             ''')
conn.commit()

curr.execute('''
             SELECT course_name,course_instructor,topic,course_duration,course_fees
             FROM courses1
             INNER JOIN course_admin
             ON courses1.course_id=course_admin.course_id;
             ''')
conn.commit()
rows=curr.fetchall()
for row in rows:
    print(row)
conn.close()