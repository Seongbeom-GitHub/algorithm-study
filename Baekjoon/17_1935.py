# 백준 1935번 "후위표기식2"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 실패
# 이해도 : 중 (피연산자를 ord를 통해 정확히 맵핑하는 부분, 소수점 포맷팅 부분 다소 생소했음)
# 소요 시간 : 학습목적 (측정하지 않음)

n = int(input())
f = input()

# 연산자 목록
op = ['+', '-', '/', '*']

# 피연산자에 대한 값을 저장할 리스트
values = [0] * 26  # A~Z에 대한 값을 저장
for i in range(n):
    values[i] = int(input())

stackResult = []

for i in f:
    if i not in op:  # 연산자가 아닌 경우
        # A는 values[0], B는 values[1], ..., Z는 values[25]에 매핑
        stackResult.append(values[ord(i) - ord('A')])
    else:
        # 스택에서 두 개의 피연산자를 꺼냄
        y = stackResult.pop()
        x = stackResult.pop()

        # 연산 수행
        if i == '+':
            stackResult.append(x + y)
        elif i == '-':
            stackResult.append(x - y)
        elif i == '/':
            stackResult.append(x / y)
        elif i == '*':
            stackResult.append(x * y)

# 결과 출력
print(f"{stackResult[0]:.2f}")
