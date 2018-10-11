#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:23:05 2018

@author: Mac
"""

#Print the last two rows in the last two columns to the Python terminal
import pandas as pd
data = pd.read_csv('iris.csv')
print('These are the last two rows in the last two columns of iris.csv:')
print(data.iloc[148:150,3:5])
print('\n')

#Get the number of observations for each species located in the data set
from collections import Counter
species=data.iloc[:,4]
print('Below is a counter for each species in the data set:')
print(Counter(species))
print('\n')

#Get the rows with Sepal.Width > 3.5
print('The rows with Sepal.Width greater than 3.5 are:')
print(data[data['Sepal.Width'] > 3.5])
print('\n')

#Write data for columns w/ setosa to 'setosa.csv'
setosa = data[data['Species'] == "setosa"]
setosa.to_csv('setosa.csv')
print('All of the columns including setosa have been written to setosa.csv in your current working directory')
print('\n')

#Calculate mean, minimum, and maximum of Petal.Length 
#for observations from virginica
virginica = data[data['Species'] == 'virginica']
petalLength = virginica.iloc[:,2]
print('The minimum petal length is:',petalLength.min())
print('The maximum petal length is:',petalLength.max())
print('The mean petal length is:',petalLength.mean())
