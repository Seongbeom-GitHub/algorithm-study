# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 349p
# Q19. 연산자 끼워 넣기
# 풀이일 : 2023-11-15
# 난이도 : 2.0/3.0
# 시간 제한 : 2초
# 메모리 제한 512MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 
# https://acmicpc.net/problem/14888

n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())  

min_value = 1e9
max_value = -1e9

def dfs(i, now) :
    global min_value, max_value, add, sub, mul, div
    
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n :
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else :
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0 :
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)