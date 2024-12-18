import numpy as np
from scipy.stats import ttest_1samp

# 데이터
scores = [75, 80, 68, 72, 77, 82, 81, 79, 70, 74, 76, 78, 81, 73, 81, 78, 75, 72, 74, 79, 78, 79]

m = 75

t,p = ttest_1samp(scores,m,alternative="greater")
print(t,p)
