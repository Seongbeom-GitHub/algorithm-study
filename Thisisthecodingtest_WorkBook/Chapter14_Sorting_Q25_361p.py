# "이것이 코딩 테스트다" / 챕터14 / Sorting / 361p
# Q25. 실패율
# 풀이일 : 2023-12-02
# 난이도 : 1.0/3.0 
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 실패
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가 시키며
    for i in range(1, N + 1) :
        # 해당 스테이지에 머문 사람수
        count = stages.count(i)

        # 실패율 계산
        if length == 0 :
            fail = 0
        else :
            fail = count / length

        answer.append((i, fail))
        length -= count
    
    # 실패율 기준으로 내림차순 정렬
    answer = sorted(answer, key = lambda t : t[1], reverse = True)

    answer = [i[0] for i in answer]
    
    
    
    return answer