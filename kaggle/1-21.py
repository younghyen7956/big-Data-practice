import pandas as pd

df1 = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

df = df1[~(df1['age']<=0)&(df1['age']==round(df1['age'],0))]

df['range'] = pd.qcut(df['age'], q=3, labels=['group1','group2','group3'])

g1_med = df[df['range'] == 'group1']['age'].median()
g2_med = df[df['range'] == 'group2']['age'].median()
g3_med = df[df['range'] == 'group3']['age'].median()

print(g1_med + g2_med + g3_med)





