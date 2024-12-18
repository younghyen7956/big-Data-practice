import pandas as pd

df = pd.read_csv(r"/data/rescue.csv", encoding="euc-kr")

df['new'] = abs((df['dclr_hour']*60+df['dclr_min'])-(df['spt_arvl_hour']*60+df['spt_arvl_min']))

print(df.sort_values('new',ascending=False).iloc[0,:].iloc[0])
print(df['new'].mean())

