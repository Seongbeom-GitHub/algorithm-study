# "이것이 코딩 테스트다" / 챕터12 / 구현 / 335p
# Q14. 외벽 점검
# 풀이일 : 2023-10-17
# 난이도 : 3.0/3.0
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 50분
# 소요 시간 : 
# https://programmers.co.kr/learn/courses/30/lessons/60062

# 1) 나의 풀이

# def solution(n, weak, dist):
#     answer = 0
    
#     dist.sorted()

#     # 친구를 거리가 긴 순서로 한명씩 꺼내서
#     for friend in range(len(dist)) :
#         # 모든 위치 대입 -> 최대로 보수 할 수있는 위치 파악 후 다음 친구
#         checkCount = 0
#         for i in range(n) :
#             if i == range

#         # 더 이상 보수 할 곳이 없으면 결과값 리턴

#         # 친구가 부족하면 리턴 -1
    
    
    
#     return answer

# 2) 모범 답안
from itertools import permutations

def solution(n, weak, dist) :
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1

    # 0부터 length - 1 까지의 위치를 각각 시작점으로 설정
    for start in range(length) :
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))) :
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length) :
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index] :
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist) : # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist) : 
        return -1
    return answer