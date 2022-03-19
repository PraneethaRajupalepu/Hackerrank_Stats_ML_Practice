'''
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.

Output Format

In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 5.5
'''
#using Linear regression model
import numpy as np
import math
from sklearn import linear_model

x = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
y = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

x = np.array(x)
y = np.array(y)

x = x.reshape(10, 1)
y = y.reshape(10, 1)

regr = linear_model.LinearRegression()
regr.fit(x, y)

test = float(input())
test = np.array(test)
test = test.reshape(1, 1)

result = regr.predict(test)
print(round(result,1))
