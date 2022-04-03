'''
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute the slope of the line of regression obtained while treating Physics as the independent variable.
Compute the answer correct to three decimal places.
'''
import math
import statistics as st
#mean function
def mean1(x):
    meanx = sum(x)/len(x)
    return meanx
#variance function
def variance1(x):
    sum1 = 0
    x_mean = sum(x)/len(x)
    var = sum(((i-x_mean)**2) for i in x)
    return var
#covariance function
def covariance1(x,y):
    return sum((a - x_mean) * (b - y_mean) for (a,b) in zip(x,y))

x = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
y = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

n = len(x)

x_mean = mean1(x)
y_mean = mean1(y)

var = variance1(x)

cov = covariance1(x,y)
# slope formula--> slope = Σ(x - mean(x)) * (y - mean(y)) / Σ (x - mean(x))²
slope = cov / var

print(round(slope,3))
