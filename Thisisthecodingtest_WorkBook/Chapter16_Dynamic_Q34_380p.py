# "이것이 코딩 테스트다" / 챕터16 / Dynamic Programming / 380p
# Q34. 병사 배치하기
# 풀이일 : 2023-12-14
# 난이도 : 1.5/3.0 
# 시간 제한 : 1초
# 메모리 제한 256MB
# 풀이 제한 시간 : 40분
# 소요 시간 : 
# https://www.acmicpc.net/problem/18353


n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n) :
    for j in range(0, i) :
        if array[j] < array[i] :
            dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))