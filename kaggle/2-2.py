import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv(r"A:\big-Data-practice\data\diabetes_train.csv")
test = pd.read_csv(r"A:\big-Data-practice\data\diabetes_test.csv")

sc = StandardScaler()

xtarget = train['Outcome']

train1 = train.drop(columns=['Outcome','id'])
test = test.drop(columns='id')

train1 = sc.fit_transform(train1)
test1 = sc.fit_transform(test)

model = RandomForestClassifier()
model.fit(train1,xtarget)
pred = model.predict_proba(test1)
pred1 = pred[:,1]
output = pd.DataFrame({'pred': pred1})
# output.to_csv('result.csv',index=False)
print(pred1,output)



