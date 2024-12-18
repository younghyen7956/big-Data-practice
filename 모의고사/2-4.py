import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve,
    f1_score,
    precision_score,
    recall_score
)

# 데이터 로드
df = pd.read_csv(r"A:\big-Data-practice\data\train_commerce.csv")

# 범주형 변수 인코딩 (pd.factorize 사용)
df['Warehouse_block'] = pd.factorize(df['Warehouse_block'])[0].astype(int)
df['Mode_of_Shipment'] = pd.factorize(df['Mode_of_Shipment'])[0].astype(int)
df['Product_importance'] = pd.factorize(df['Product_importance'])[0].astype(int)
df['Gender'] = pd.factorize(df['Gender'])[0]

# 입력 변수(X)와 타겟 변수(Y) 정의
x = df[['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']]
y = df['Reached.on.Time_Y.N'].astype('category')

# 데이터 분리
trainx, testx, trainy, testy = train_test_split(x, y, test_size=0.2, random_state=42)

# 모델 생성 및 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(trainx, trainy)

# 예측 및 평가
pred = model.predict(testx)  # 테스트 데이터로 예측
pred_proba = model.predict_proba(testx)[:, 1]  # 양성 클래스 확률

# 혼동 행렬과 분류 보고서
conf = confusion_matrix(testy, pred)
print("Confusion Matrix:")
print(conf)
print("\nClassification Report:")
print(classification_report(testy, pred))

# 피처 중요도
print("Feature Importances:")
print(model.feature_importances_)

# F1, Precision, Recall
print(f"F1 Score: {f1_score(testy, pred)}")
print(f"Precision: {precision_score(testy, pred)}")
print(f"Recall: {recall_score(testy, pred)}")

# ROC AUC
roc_auc = roc_auc_score(testy, pred_proba)
print(f"ROC AUC: {roc_auc}")

# ROC Curve
fpr, tpr, thresholds = roc_curve(testy, pred_proba)
print("FPR:", fpr)
print("TPR:", tpr)
