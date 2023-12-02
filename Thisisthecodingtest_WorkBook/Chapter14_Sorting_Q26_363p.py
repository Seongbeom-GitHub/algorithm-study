# "이것이 코딩 테스트다" / 챕터14 / Sorting / 363p
# Q26.카드 정렬하기
# 풀이일 : 2023-12-02
# 난이도 : 2.0/3.0 
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 실패
# https://acmicpc.net/problem/1715

import heapq

n = int(input())    

# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n) :
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙에 원소가 1개 남을 때까지
while len(heap) != 1 :
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
