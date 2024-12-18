from scipy.stats import chisquare

# 관측된 빈도
observed_frequencies = [30, 60, 50, 40, 20]

# 기대된 빈도
expected_frequencies = [200 * 0.20, 200 * 0.30, 200 * 0.25, 200 * 0.15, 200 * 0.10]

# 카이제곱 검정
chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)

print(chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies))