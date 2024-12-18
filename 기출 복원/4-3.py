import pandas as pd

df = pd.read_csv(r"/data/student.csv", encoding="euc-kr")

df['new'] = df['전입학생수합계(명)']-df['전출학생수합계(명)']

print(df.sort_values('new',ascending=False).head(1).loc[:,('전체학생수합계(명)','new')])