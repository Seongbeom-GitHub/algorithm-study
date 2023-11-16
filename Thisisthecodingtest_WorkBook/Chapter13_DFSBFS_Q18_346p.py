# "이것이 코딩 테스트다" / 챕터13 / DFS BFS / 346p
# Q18. 괄호 변환
# 풀이일 : 2023-11-02
# 난이도 : 1.0/3.0
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 실패
# https://programmers.co.kr/learn/courses/30/lessons/60058


# 균형 잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p) : 
    count = 0 # 왼쪽 괄호 개수
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p) :
    count = 0 # 왼쪽 괄호의 개수
    for i in p :
        if i == '(' :
            count += 1
        else :
            # 닫을 왼쪽 괄호가 0이면 False
            # 쌍이 맞지 않으면 False 반환
            if count == 0 : 
                return False
            count -= 1
    return True

def solution(p) :
    answer = ''
    if p == '' :
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # 올바른 괄호 문자열이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u) :
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)) :
            if u[i] == '(' :
                u[i] = ')'
            else :
                u[i] = '('
        answer += "".join(u)

    return answer
