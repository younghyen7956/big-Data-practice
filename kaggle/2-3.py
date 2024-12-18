import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv(r"A:\big-Data-practice\data\adult.csv")

x = df.drop(columns="income")
y = df['income']
df['workclass'] = df['workclass'].fillna(df['workclass'].mode()[0])
df['occupation'] = df['occupation'].fillna("null")
df['native.country'] = df["native.country"].fillna(df['native.country'].mode()[0])
x = pd.get_dummies(x)
trainx, testx, trainy, testy = train_test_split(x,y,test_size=0.2,random_state=42)
# print(trainx.columns)

sc = StandardScaler()
trainx = sc.fit_transform(trainx)
testx = sc.fit_transform(testx)

# target값 변경
y = (y!= '<=50K').astype(int)
print(y[:5])

model = RandomForestClassifier(random_state = 2022)
model.fit(trainx, trainy)
pred = model.predict(testx)
print('accuracy score:', (accuracy_score(testy, pred)))
# print(trainx)