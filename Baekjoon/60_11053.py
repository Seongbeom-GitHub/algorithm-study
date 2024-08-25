# https://www.acmicpc.net/problem/11053
# 문제 분류 : 알고리즘 기초 1/2 (다이나믹프로그래밍)
# 풀이 : 답안참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n) :
    for j in range(i) :
        if arr[j] < arr[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))