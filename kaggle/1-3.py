import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\basic1.csv")

# print(df.isnull().sum()/df.shape[0])

df1 = df.drop(['f3'], axis=1)

s=df[df['city']=='서울']['f1'].median()
k=df[df['city']=='경기']['f1'].median()
b=df[df['city']=='부산']['f1'].median()
d=df[df['city']=='대구']['f1'].median()
df['f1'] = df['f1'].fillna(df['city'].map({'서울':s,'경기':k,'부산':b,'대구':d}))
