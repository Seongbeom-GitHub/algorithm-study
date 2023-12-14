# "이것이 코딩 테스트다" / 챕터16 / Dynamic Programming / 377p
# Q33. 퇴사
# 풀이일 : 2023-12-14
# 난이도 : 2.0/3.0 
# 시간 제한 : 2초
# 메모리 제한 512MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 
# 문제 출처 : 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/14501

n = int(input()) # 전체 상담 개수
t = [] # 각 상담의 기간
p = [] # 각 상담의 보상 금액
dp = [0] * (n + 1) # 1차원 dp 테이블
max_value = 0

for _ in range(n) :
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1) :
    # time = i번째 상담에 걸리는 시간 + 이전에 보낸 시간
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n :
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]

    # 상담이 기간을 벗어나는 경우
    else : 
        dp[i] = max_value

print(max_value)