# 백준 17413번 "단어 뒤집기2"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 중상 (스택 사용 + 구현부분)
# 소요 시간 : 학습목적 (측정하지 않음)

s = input()

result = []
stack = []
isTag = False

for str in s :
    if str == '<' :
        while stack : # 태그가 시작되면 태그 전까지의 문자열을 뒤집어서 result에 추가
            result.append(stack.pop())
        isTag = True
        result.append(str)
    elif str == '>' :
        isTag = False
        result.append(str)
    elif isTag : # 태그 모드일때는 result에 바로 추가 
        result.append(str)
    elif str == ' ' : 
        while stack :
            result.append(stack.pop())
        result.append(str)
    else : # 태그가 아닌 문자는 스택에 넣기
        stack.append(str)

# 스택안에 남아있는 문자들을 pop
while stack : 
    result.append(stack.pop())

print(''.join(result))