'''
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.
'''
# Solution #1:

from scipy.stats import pearsonr
x = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
y = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]
corr,_ = pearsonr(x,y)
print(round(corr,3))

# Solution #2:

import math
import statistics as st

x = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
y = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

n = len(x)

x_mean = st.mean(x)
y_mean = st.mean(y)

x_std = st.stdev(x)
y_std = st.stdev(y)

cov = sum((a - x_mean) * (b - y_mean) for (a,b) in zip(x,y)) 

coeff = cov / (n*x_std*y_std)

print(round(coeff,3))
