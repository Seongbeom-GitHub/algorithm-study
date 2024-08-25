# 백준 11726번 "2*n 타일링"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 부분참고
# 이해도 : 높음 
# 소요 시간 : 학습목적 (측정하지 않음)


n = int(input())

if n < 1:
    print(0)  
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n] % 10007)
