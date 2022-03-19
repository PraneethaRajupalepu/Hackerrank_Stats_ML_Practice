'''
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.

Output Format

In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 5.5
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import statistics as st

x = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
y = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

x_mean = st.mean(x)
y_mean = st.mean(y)

x_var = st.variance(x)
y_var = st.variance(y)

cov = sum((a - x_mean) * (b - y_mean) for (a,b) in zip(x,y)) / len(x)

slope = cov / x_var
intercept = y_mean - slope * x_mean

result = slope * 10 + intercept
print(round(result,1))
