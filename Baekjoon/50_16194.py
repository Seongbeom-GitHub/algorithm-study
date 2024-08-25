# 백준 16194번 "카드 구매하기 2"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 답안참고
# 이해도 : 중간
# 소요 시간 : 학습목적 (측정하지 않음)

'''
카드 구매하기 1번 문제와 동일한 방식으로 점화식 세우기
(2중 반복문으로 dp 테이블을 만든다)
'''

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [float('inf')] * (n + 1)

dp[0] = 0
dp[1] = p[1]

for i in range(1, n + 1) :
    for j in range(1, i + 1) :
        dp[i] = min(dp[i], dp[i - j] + p[j])

print(dp[n])