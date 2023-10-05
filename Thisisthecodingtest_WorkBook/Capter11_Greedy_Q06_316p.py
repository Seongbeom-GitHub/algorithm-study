# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 316p
# Q06. 무지의 먹방 라이브
# 풀이일 : 2023-10-05
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 33분 (실패)


# 1) 나의 풀이 (실패)
def solution(food_times, k):
    answer = 0
    c = 0
    count = 0
    for i in range(k) :
        
        if c > len(food_times) :
            c = 0

        # 0값이면 인덱스값 증가
        if food_times[c] == 0 :

            # 배열 전체가 0인지 파악
            count += 1
            if count >= len(food_times) :
                answer = -1
                break

            # 이번 인덱스만 0이면 다음 인덱스로
            c += 1

        food_times[c] -= 1

        c += 1

    if c > len(food_times) :
        c = 0
    answer = food_times[c]    
    return answer