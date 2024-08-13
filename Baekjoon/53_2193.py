# 백준 2193번 "이친수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 직접풀이
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)


n = int(input())

# N이 0일 경우 처리
if n == 0:
    print(0)
    exit()

dp = [0] * (n + 1)

# 초기값 설정
dp[1] = 1
if n >= 2:
    dp[2] = 1

# DP 테이블 채우기
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# 결과 출력
print(dp[n])
