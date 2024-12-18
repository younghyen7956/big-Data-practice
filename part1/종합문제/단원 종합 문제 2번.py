import pandas as pd
import os
from pathlib import Path

current_file_path = Path(__file__)

directory = current_file_path.parent.parent

file_path = directory/"data"/"mtcars.csv"

df = pd.read_csv(file_path)
df1= df[df['am']==1]
print(df1[df1['cyl']==4]['mpg'].mean()+df1[df1['cyl']==4]['hp'].std())
# print(df)