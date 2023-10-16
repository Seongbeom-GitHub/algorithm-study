# "이것이 코딩 테스트다" / 챕터12 / 구현 / 332p
# Q13. 치킨 배달
# 풀이일 : 2023-10-16
# 난이도 : 2.0/3.0
# 시간 제한 : 1초
# 메모리 제한 512MB
# 풀이 제한 시간 : 40분
# 소요 시간 : 
# https://www.acmicpc.net/problem/15686


# 1) 나의 풀이
# from itertools import combinations

# n, m = map(int, input().split())
# city = []
# home = []
# chicken = []

# for _ in range(n) :
#     a = list(map(int, (input().split())))
#     city.append(a)

# # 집과 치킨집의 위치를 저장하는 배열
# for x in range(n) :
#     for y in range(n) :
#         if city[x][y] == 1 :
#             home.append((x,y))
#         if city[x][y] == 2 :
#             chicken.append((x,y))
        
# for i in range(1, m + 1) :
#     comb = list(combinations(chicken, i))
#     for x in range(len(home)) :
#         for y in range(len(home[0])) :
#             abs(home[x] - chicken[x]) + abs(home[y] - chicken[y])

# 2) 모범 답안
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n) :
    data = list(map(int, input().split()))
    for c in range(n) :
        if data[c] == 1 :       # 집
            house.append((r,c))
        elif data[c] == 2 :     # 치킨집
            chicken.append((r,c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidates) :
    result = 0
    # 모든 집에 대하여
    for hx, hy in house :
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidates :
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리 구하기
        result += temp
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates :
    result = min(result, get_sum(candidate))

print(result)