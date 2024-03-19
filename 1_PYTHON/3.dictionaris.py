# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:10:57 2023

@author: Hp
"""
#removing from list
another_lst = ['Gary','MArk','Sham','sam']
print(another_lst)
another_lst.remove('MArk')
print(another_lst)

#pop method
another_lst = ['Gary','MArk','Sham','sam']
print(another_lst)
print(another_lst.pop(2))
print(another_lst)

#inserting into the list
another_lst = ['Gary','MArk','Sham','sam']
print(another_lst)
another_lst.insert(2,'apple')
print(another_lst)

#list concat
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = l2 + l1
print(l3)


#SET 

s1 =  {'apple','mango','banana','apple'}
print(s1)

#for accessing elements in set
#for item in s1:    
#adding item in set
s1 =  {'apple','mango','banana','apple'}
s1.add('lichi')
print(s1)
s1.update(['orange','grapefruit'])
print(s1)

#finding lenth of set
print(len(s1))

#optining max and min values in set
s2 = {1,2,3,4,5,6,78}
print(max(s2))
print(min(s2))

#removing an item
s1 =  {'apple','mango','banana','apple'}
print(s1)
s1.remove('apple')
s1.discard('mango')
print(s1)

#set operations

s1 = {'apple','banana'}
s2 = {'mango','lichi','apple'}
print('Union:',s1 | s2)
print('Intersection:',s1 & s2)
print('difference:',s1 - s2)
print('difference:',s2 - s1)
###############################################

#DICTIONARIES
capitals={'maharashtra':'Mumbai',
          'Gujrat':'Surat',
          'Up':'Lakhnow',
          'Kanataka':'Banglore',
          'AP':'hydrabad'
          }
print(capitals)

#accessing items
print('capitals[maharashtra]:',capitals['maharashtra'])

#add
capitals['west bengal']='kolkata'
print(capitals)

#removing entry
#pop
print(capitals.pop('AP'))
print(capitals)

del capitals['Up']
print(capitals)

#changing key value
capitals['Gujrat'] = 'Gandhinagar'
print(capitals)

#iterting over keys
capitals={'maharashtra':'Mumbai',
          'Gujrat':'Surat',
          'Up':'Lakhnow',
          'Kanataka':'Banglore',
          'AP':'hydrabad'
          }

for i in capitals:
    print(i , end=', ')

    
for i in capitals:
    print(i , end=', ')
    print(capitals[i])
    
#values,keys,items
print(capitals.values())
print(capitals.keys())
print(capitals.items())

#checking key members
print('Up' in capitals )
print('Bihar' in capitals)

#cheking key membership
print(len(capitals))

#dictionaries can have values in tuple
seasons = {'Summer':('feb','march','april','may'),
           'rainy' :('june','july','august','september'),
           'winter':('october','nov','decmber','january')
            }
print(seasons['rainy'])
print(seasons['rainy'][1])

#dictionaries in list
seasons = {'Summer':['feb','march','april','may'],
           'rainy' :['june','july','august','september'],
           'winter':['october','nov','decmber','january']
            }
print(seasons)


#get() is useful method to access values of key in dictionary
print(capitals.get('Up'))

#duplicates not allow in dictionary
#duplicaye can not have same items with the same key
dict1 ={
        'brand':'Maruti',
        'model':'Brezza',
        'year':2020,
        'year':2021
        }
print(dict1)

#loop through a dictionary it will be show only keys
for x in dict1:
    print(x)
    
#print all the values in dictionaries one by one shows values
for x in dict1:
    print(dict1[x])
    
#you can also use the values() method to return values
for x in dict1.values():
    print(x)
    
#also use the keys() to show keys
for x in dict1.keys():
    print(x)

#loop through both keys and values
for x,y in dict1.items():
    print(x,y)
    
#copy a dictionary
#make a copy of dictionary with the copy()

mydict = dict1.copy()
print(mydict)

        
