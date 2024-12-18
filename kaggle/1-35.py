import pandas as pd

df = pd.read_csv(r"A:\big-Data-practice\data\e-commerce.csv")
df['new'] = df['Feedback'].str.len()

# print(df[df['new']==df['new'].max()])
#
# idx = df['new'].idxmax()
# user = df.iloc[idx]['UserID']
# print(df[df['UserID']==user])

# print(df)

print(df.groupby('Category')['Feedback'].apply(lambda x: x.str.contains('제품').sum()))