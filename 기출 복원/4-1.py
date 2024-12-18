import pandas as pd

df = pd.read_csv(r"/data/garbagebag.csv", encoding="euc-kr")

df1 = df[(df['종량제봉투처리방식']=="소각용")&(df['종량제봉투사용대상']=="가정용")&(df['2L가격']!=0)]

print(df1['2L가격'].mean())