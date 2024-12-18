import pandas as pd
from scipy import stats
from scipy import stats
df = pd.read_csv(r"A:\big-Data-practice\data\recordmath.csv")

m = df[df['sex']=='Male']
f = df[df['sex']=='Female']

d1 = m[m['academy']==1]
d2 = f[f['academy']==1]

print(len(d1)/len(m))
print(len(d2)/len(f))

result = [[len(d1),len(d2)],[len(m)-len(d1),len(f)-len(d2)]]

chi,p,d,e = stats.chi2_contingency(result)

print(chi,p)
