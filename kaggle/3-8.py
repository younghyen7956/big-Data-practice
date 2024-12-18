import pandas as pd
from scipy import stats

df = pd.DataFrame({
    'A':[77, 75, 82, 80, 81, 83, 84, 76, 75, 87],
    'B':[80, 74, 77, 79, 71, 74, 78, 69, 70, 72],
})

t,p = stats.ttest_ind(df['A'],df['B'])

print(t,p)

f,p1 = stats.f_oneway(df['A'],df['B'])

print(f,p1)