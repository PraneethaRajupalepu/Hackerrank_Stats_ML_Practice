#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Charlie wants to purchase office-space. He does a detailed survey of the offices 
and corporate complexes in the area, and tries to quantify a lot 
of factors, such as the distance of the offices from residential and 
other commercial areas, schools and workplaces; the reputation of the 
construction companies and builders involved in constructing the apartments; 
the distance of the offices from highways, freeways and important roads; 
the facilities around the office space and so on.

There is one important observation which Charlie has made: The prices per square foot, are (approximately)
a polynomial function of the features in the observation table. This polynomial always has an order less than 4 

##Based on above statement it is finalised to consider polynomial features degree as 3( less than 4)
'''

# Import libraries
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Set data
features, rows = map(int, input().split())
train, y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            y.append(elements[j])
    train.append(x)

# Set Polynomial Features
poly = PolynomialFeatures(degree=3)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(poly.fit_transform(np.array(train)), y)

# Get the parameters X for discovery the Y
new_rows = int(input())
test = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    test.append(x)

# Gets the result and show on the screen
result = model.predict(poly.fit_transform(np.array(test)))
for i in range(len(result)):
    print(round(result[i],2))

