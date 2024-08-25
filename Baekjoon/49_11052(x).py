# 백준 11052번 "카드 구매하기"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 답안참고 (이해 안됨)
# 이해도 : 낮음 
# 소요 시간 : 학습목적 (측정하지 않음)

'''
dp테이블 이전 값에서 -j 반복을 통해 최적의 값을 찾는 점화식 세우기
'''

# 1. 처음 접근 방식
# n = int(input())
# p = list(map(int, input().split()))
# onePrice = []

# totalSum = 0

# for i in range(len(p)):
#     onePrice.append((i + 1, (p[i] / (i + 1))))


# onePrice.sort(key=lambda x: x[1], reverse=True)

# target = 0

# while n > 0 and target < len(onePrice):
#     if n - onePrice[target][0] >= 0:
#         totalSum += p[onePrice[target][0] - 1]
#         n -= onePrice[target][0]
#     else:
#         target += 1

# print(totalSum)


# 2. 모범답안
N = int(input())

P = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

dp[1] = P[1]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + P[j]:
            dp[i] = dp[i - j] + P[j]
        # dp[i] = max(dp[i], dp[i - j] + P[j]) 위의 if문을 다음과 같이 한줄로도 가능 단, 시간복잡도 보장x

print(dp[N])
