import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc, RocCurveDisplay
import matplotlib.pyplot as plt

# 데이터 로드 및 DataFrame 생성
rdf = load_iris()
df = pd.DataFrame(data=np.c_[rdf['data'], rdf['target']],
                  columns=rdf['feature_names'] + ['target'])

# 무작위로 데이터를 나누되 클래스 비율 유지 (stratify)
trainx, testx, trainy, testy = train_test_split(
    df.drop(columns='target'), df['target'], test_size=0.3, random_state=42, stratify=df['target']
)

# 스케일링
sc = StandardScaler()
trainx = sc.fit_transform(trainx)
testx = sc.transform(testx)

# 하이퍼파라미터 설정 및 모델 학습
par = {'kernel': ['rbf'],
       'C': [0.1, 1, 10, 100],
       'gamma': [0.1, 0.5, 1, 2]}

model = SVC(probability=True)  # ROC 커브 및 AUC를 위해 `probability=True` 설정
grid = GridSearchCV(model, par, cv=5, n_jobs=1)
grid.fit(trainx, trainy)

# 최적 하이퍼파라미터 및 정확도 출력
print(grid.best_params_)
bmodel = grid.best_estimator_
accuracy = bmodel.score(testx, testy)
print(f"Accuracy: {accuracy}")

# 1. 혼동 행렬
predictions = bmodel.predict(testx)
cm = confusion_matrix(testy, predictions)
print(f"Confusion Matrix:\n{cm}")

# 2. ROC 커브 및 AUC 계산
# SVM은 다중 클래스이므로 각 클래스에 대해 ROC 커브를 그릴 수 있음
y_score = bmodel.predict_proba(testx)  # 클래스별 확률 점수
fpr = {}
tpr = {}
roc_auc = {}

for i in range(3):  # Iris 데이터는 3개의 클래스
    fpr[i], tpr[i], _ = roc_curve(testy == i, y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Macro AUC
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(3)]))
mean_tpr = np.zeros_like(all_fpr)
for i in range(3):
    mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
mean_tpr /= 3
macro_auc = auc(all_fpr, mean_tpr)
print(f"Macro AUC: {macro_auc}")

# 3. ROC 커브 그리기
plt.figure()
for i in range(3):
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.2f})")
plt.plot([0, 1], [0, 1], 'k--', label="Random Guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.show()
