# "이것이 코딩 테스트다" / 챕터16 / Dynamic Programming / 376p
# Q32. 정수 삼각형
# 풀이일 : 2023-12-14
# 난이도 : 1.5/3.0 
# 시간 제한 : 2초
# 메모리 제한 128MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 
# 문제 출처 : IOI 1994년도

n = int(input())
dp = []

for _ in range(n) :
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
for i in range(1, n) :
    for j in range(i + 1) :
        # 왼쪽 위에서 내려오는 경우
        if j == 0 :
            up_left = 0
        else :
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i :
            up = 0
        else :
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))