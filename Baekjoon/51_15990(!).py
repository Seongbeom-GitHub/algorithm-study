# 백준 15990번 "1, 2, 3 더하기 5"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 낮음
# 소요 시간 : 학습목적 (측정하지 않음)

'''
2차원 배열을 이용해 1,2,3번째 수의 dp테이블에 각각 1,2,3으로 끝나는 경우의 수를 저장한다.
n번째 수는 n이전의 3가지 dp테이블에서 숫자를 연속해서 뽑는 경우를 제외하고 경우의 수를 더해 구한다.
'''


import sys

input = sys.stdin.readline
MAX_N = 100001
MOD = 1000000009

T = int(input())

dp = [[0 for _ in range(3)] for i in range(MAX_N)]

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, MAX_N):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][1] = (dp[i - 2][2] + dp[i - 2][0]) % MOD
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % MOD
# 나머지를 저장하지 않으면 값이 너무 커져 시간초과가 뜸

for j in range(T):
    n = int(input())
    print(sum(dp[n]) % MOD)
    # 마지막에도 나머지 연산을 해줘야 틀리지 않음
