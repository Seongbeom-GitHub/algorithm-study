# "이것이 코딩 테스트다" / 챕터12 / 구현 / 323p
# Q09. 문자열 압축
# 풀이일 : 2023-10-07
# 난이도 : 1.5/3.0
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 42분 실패

# https://school.programmers.co.kr/learn/courses/30/lessons/60057


# 1) 나의 풀이
# def solution(s):
#     slist = list(map(str, s))
#     answer = 0
#     unit = len(slist) // 2
#     slength = [] * (unit + 1) # 각 압축 길이별 문자열 길이를 담는 배열 초기화
#     # 0부터 반으로 나누는 수까지 반복
#     for i in range(0, unit + 1) :
#         temp = []
#         a = ""
#         for j in range(i) :
#             a += slist[j]

#         temp.append(a)

#         for x in range(0, temp -1) :
#             count = 0
#             if temp[x] == temp[x+1] :
#                 count += 1
#             else :
#                 if count < 1 : 
#                     slength.append(len(str(count) + temp[x]))
#                     count = 0
#                 else :
#                     slength.append(len(temp[x]))
#                     count = 0
#         temp.clear()
#     answer = min(slength)

#     return answer

# 2) 모범답안
def solution(s) :
    answer = len(s)
    # 1개 단위 (step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2 + 1) :
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) :
        # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step] :
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else :
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

