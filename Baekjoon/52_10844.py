# 백준 10844번 "쉬운 계단 수"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 답안참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)

'''
바텀 업 방식의 동적 프로그래밍을 통해 해결 가능
'''

MOD = 1000000000

n = int(input())
total = 0

dp = [[0] * 10 for _ in range(n + 1)]

# 길이가 1인 계단수 초기화
for i in range(1, 10) :
    dp[1][i] = 1

# DP 테이블 채우기
for j in range(2, n + 1) :
    dp[j][0] = dp[j - 1][1] # 마지막 숫자가 0일때

    for k in range(1, 9) : # 마지막 숫자가 1 ~ 8 일때
        dp[j][k] = dp[j - 1][k -1] + dp[j - 1][k + 1]

    dp[j][9] = dp[j - 1][8] # 마지막 숫자가 9일때

total = sum(dp[n]) % MOD

print(total)