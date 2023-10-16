# "이것이 코딩 테스트다" / 챕터12 / 구현 / 329p
# Q12. 기둥과 보 설치
# 풀이일 : 2023-10-10
# 난이도 : 1.5/3.0
# 시간 제한 : 5초
# 메모리 제한 128MB
# 풀이 제한 시간 : 50분
# 소요 시간 : 
# https://programmers.co.kr/learn/courses/30/lessons/60061

# 2) 모범 답안

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer) :
    for x, y, stuff in answer :
        if stuff == 0 : # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x -1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer :
                continue
            return False # 아니라면 거짓 반환
        elif stuff == 1 : # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결' 이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer) :
                continue
            return False # 아니라면 거짓 반환
    return True

def solution(n, build_frame) :
    answer = []
    for frame in build_frame : # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0 : # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer) :
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1 : # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치
            if not possible(answer) :
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니면 다시 제거
    return sorted(answer)