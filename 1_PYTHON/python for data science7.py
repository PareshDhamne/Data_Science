# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:01:17 2023

@author: Hp
"""

#MATPLOTLIB
import matplotlib.pyplot as plt
plt.plot([1,3,2,5,4])
plt.show()

####################################

#Multiline plots
import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi*1.5 for xi in x])  
plt.plot(x,[xi*3.0 for xi in x])  
plt.plot(x,[xi/3.0 for xi in x])  
plt.show()
#######################################
'''
#note how matplotlib automaticallly
chooses different color
for each line green for
the first line blue for the second line
and red for the third one
'''

#grid ,axes, and labels
#adding a grid
import matplotlib.pyplot as plt
import numpy as np
x= np.arange(1,5)
plt.plot(x,x*1.5,x ,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()
############################
#handling axes
import matplotlib.pyplot as plt
import numpy as np
x= np.arange(1,5)
plt.plot(x,x*1.5,x ,x*3.0,x,x/3.0)

plt.axis() #show the current axis limits values
plt.axis([0,5,-1,13]) #set new axis limits
#[xmin,xmax,ymin,ymax]
#[0,5,-1,13]
plt.show()
##########################################

#Adding labels
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel('THis is the X axis')
plt.ylabel('This is the y axis')
plt.show()

#Adding atitle
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple plot')
plt.show()
########################################

#Adding a legend
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()
#################################
#control colors
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()
#####################################

#specifying styles in multiline plot
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()
######################################
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()
#-- for ------ line
#-. for -.-.-. line
#: for ........line
###########################

'''
style abbrivation style
- solid line
-- dashed line
-. dahs dot line
: dotted line
'''

##############################
#Histogram charts
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()
############################
#histogram charts
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y);
plt.show()
##############################


'''
the bar( ) graph function is used to generate bar charts in matplotlab
the function execpts two list of values
the x coordinates that are the position of the bar's left
and the height of the bars:
    
as we can see the left margin of the  bars start at the points specified in the first list
while their heights are the 
'''
#scatter plot
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y);
plt.show()
#################################

size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x ,y ,s=size ,c=colors);
plt.show()
###############################

#adding text
import numpy as np
import  matplotlib.pyplot as plt
x=np.linspace(-4,4,1024)
y=.25 * (x+4.) * (x+1.) * (x-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(x,y,c='k')
plt.show()
####################################
#How to use Seborn for data visualization
#pip install seaborn
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#seaborn has 18 in built datasets
#that can be found using the following command
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()


#Count plot
'''
A counter plot ishelpful when dealing with 

'''
sns.countplot(x='sex',data=df)
#x=the name of the column
#data  dataframe
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
#it shows that how many males and femals are servived in a titinac
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')
#set is used for a prticulsr set of color apply to graph it is alreay declared

#hue = the name of categorical column to split the graphs
#palette- it is color to be used

###########################################
#KDE Plot
#A kernel Densiy Estime plot is used to plot the distribution of continous data.
sns.kdeplot(x='age',data=df,color='black')

#Distribution Plot
sns.displot(x='age',kde=True,bins=5,data=df)
sns.displot(x='age',kde=False,bins=5,data=df)
#kde it is set of false by default. However
#bins=the number of bars

sns.displot(x='age',kde=True,bins=5,
hue= df['survived'],palette='Set1',data=df)

#scatter plot
#Use iris dataset
df=sns.load_dataset('iris')
df.head

#Scatter plots hepls
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')
'''
sepal length less than 6cm and petal length less than 2 c are serosa
7cm                                                   5ch are vrsicolor
'''

#join plot
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg') #important
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

#scatter hist hex kde reg resid are kind of graph

#pair plots
sns.pairplot(df)

#a heat map can be used to visualize confusion
corr=df.corr()
sns.heatmap(corr)

##############################################

df=sns.load_dataset('iris')
df.head
