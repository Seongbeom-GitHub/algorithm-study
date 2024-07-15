# 백준 17298번 "오큰수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 하 (인덱스를 스택에 넣어 비교하는 아이디어를 떠올리기 어려웠음 / 유튜브 강의 참고함)
# 소요 시간 : 학습목적 (측정하지 않음)

n = int(input())
a = list(map(int, input().split())) # 수열
result = [-1] * n  # 결과 리스트를 -1로 초기화

stack = [] # 인덱스를 담는 스택

for i in range(n):
    while stack and a[stack[-1]] < a[i]:  # 오큰수 조건
        result[stack.pop()] = a[i] # 오큰수로 변경

    stack.append(i)

print(" ".join(map(str, result)))
