import numpy as np
import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def exam_data_load(df, target, id_name="", null_name=""):
    if id_name == "":
        df = df.reset_index().rename(columns={"index": "id"})
        id_name = 'id'
    else:
        id_name = id_name

    if null_name != "":
        df[df == null_name] = np.nan

    X_train, X_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=2021)
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[id_name, target])
    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[id_name, target])
    return X_train, X_test, y_train, y_test

df = pd.read_csv(r"A:\big-Data-practice\data\house train.csv")

df = pd.get_dummies(df, drop_first=True)  # drop_first=True로 더미 변수의 중복을 방지

# 이후 train과 test로 나누기
trainx, testx = train_test_split(df, test_size=0.2, shuffle=True, random_state=2021)
trainy = trainx[['Id', 'SalePrice']]
trainx = trainx.drop(columns=['Id', 'SalePrice'])
testy = testx[['Id', 'SalePrice']]
testx = testx.drop(columns=['Id', 'SalePrice'])

# trainx, testx, trainy, testy = exam_data_load(df, target='SalePrice', id_name='Id')
#
# trainx = trainx.select_dtypes(exclude=['object'])
# testx = testx.select_dtypes(exclude=['object'])
# target = trainy['SalePrice']

# trainx = pd.get_dummies(trainx)
# testx = pd.get_dummies(testx)
# print(trainy['SalePrice'])
# trainx = train.drop(columns='SalePrice')
# testx = test.drop(columns='SalePrice')

# trainy = train['SalePrice']
# testy = test['SalePrice']
#
s = SimpleImputer()
trainx = s.fit_transform(trainx)
testx = s.transform(testx)
#
model = RandomForestRegressor()
model1 = XGBRegressor()
#
model.fit(trainx,trainy)
model1.fit(trainx,trainy)
#
pred = model.predict(testx)
pred1= model1.predict(testx)
#
print(r2_score(testy,pred))
print(r2_score(testy,pred1))
#
print(np.sqrt(mean_squared_error(testy,pred)))
print(np.sqrt(mean_squared_error(testy,pred1)))