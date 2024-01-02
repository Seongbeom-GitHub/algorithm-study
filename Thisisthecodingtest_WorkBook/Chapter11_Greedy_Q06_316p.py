# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 316p
# Q06. 무지의 먹방 라이브
# 풀이일 : 2023-10-05
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 30분
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=phthon3

import heapq

def solution(food_times, k) :
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1 반환
    if sum(food_times) <= k :
        return -1
    
    q = []
    for i in range(len(len(food_times))) :
        # 튜플 (음식 시간, 음식 번호) 형태로 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0   # 먹기위해 사용한 시간
    previous = 0    # 직전에 다 먹은 음식 시간
    length = len(food_times)    # 남은 음식의 수

    # 먹기위해 사용한 시간 + (현재 음식의 시간 - 이전 음식의 시간) * 음식의 개수 
    # 즉, 여지것 걸린 시간 + 지금 뽑은 음식을 먹는데 걸리는 시간이 남은 k초 보다 크면 반복문 종료
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]   # 최소값을 꺼내 그 값의 [0]번째 데이터 값을 가져옴
        sum_value += (now - previous) * length
        length -= 1     # 다먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정 
    
    result = sorted(q, key =lambda x : x[1])
    return result[(k - sum_value) % length[1]]

