from scipy import stats

data = [75, 83, 81, 92, 68, 77, 78, 80, 85, 95, 79, 89]

s,p = stats.shapiro(data)

print(s,p)