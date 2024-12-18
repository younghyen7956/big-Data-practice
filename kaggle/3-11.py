from scipy.stats import poisson

# 평균 발생 횟수 (하루에 잡지를 구매하는 고객 수)
lambda_ = 3

# 하루에 정확히 5명의 고객이 잡지를 구매할 확률
print(int(poisson.pmf(5, lambda_)*100))

print(int(poisson.pmf(2, lambda_)*100))

