import pandas as pd
import os
from pathlib import Path

current_file_path = Path(__file__)

directory = current_file_path.parent.parent

file_path = directory/"data"/"mtcars.csv"

df = pd.read_csv(file_path)
df1 =df[df['am']==0]
q1 = df1['mpg'].quantile(0.25)
q3 = df1['mpg'].quantile(0.75)
iqr = q3-q1
m =  df1['mpg'].mean()
print(len(df1[(df1['mpg'] <= (m - iqr)) | (df1['mpg'] >= (m + iqr))]))
print(df1[(df1['mpg'] <= (m - iqr)) | (df1['mpg'] >= (m + iqr))]['mpg'].mean())

# print(df)