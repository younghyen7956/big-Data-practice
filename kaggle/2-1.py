import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(r"A:\big-Data-practice\data\titanic.csv")

x = df.drop(columns='Survived')
y = df['Survived']



trainx, testx, trainy,testy = train_test_split(x,y,test_size=0.2,random_state=42)

trainx1 = pd.get_dummies(trainx[['Sex','Pclass','SibSp','Parch']])

test1 = pd.get_dummies(testx[['Sex','Pclass','SibSp','Parch']])

model = RandomForestClassifier(n_estimators=200,max_depth=7,random_state=42)
model.fit(trainx1,trainy)

# print(model.predict(test1))

model.score(trainx1,trainy)
# print(test1)
output = pd.DataFrame({'PassengerId': testx.PassengerId, 'Survived': model.predict(test1)})
print(output.head())

print(model.score(test1, testy))


