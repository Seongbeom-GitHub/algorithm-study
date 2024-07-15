# 백준 10799번 "쇠막대기"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 중하 (스택과 구현을 활용하여 문제해결 방법을 구상하는것이 미숙함)
# 소요 시간 : 학습목적 (측정하지 않음)

s = input()
stack = []
cnt = 0

for i in range(len(s)) :
    if s[i] == '(' :        # 열린 괄호는 stack에 push
        stack.append('(')
    else :                   
        stack.pop()         # 닫힌 괄호는 pop
        
        if s[i-1] == '(' :  # 레이저의 경우
            cnt += len(stack)   # stack에 있는 열린괄호의 수 만큼 카운트
        else :              # 쇠막대의 끝인 경우
            cnt += 1     

print(cnt)