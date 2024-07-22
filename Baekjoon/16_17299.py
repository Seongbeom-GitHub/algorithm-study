# 백준 17299번 "오큰등수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 실패
# 이해도 : 하 (복습 필요)
# 소요 시간 : 학습목적 (측정하지 않음)

from collections import Counter

n = int(input())
a = list(map(int, input().split()))  # 수열
result = [-1] * n  # 결과 리스트를 -1로 초기화

# 각 숫자의 빈도수를 계산합니다.
frequency = Counter(a)

stack = []  # 인덱스를 담는 스택

for i in range(n):
    # 현재 스택의 맨 위에 있는 인덱스의 빈도수가 현재 숫자의 빈도수보다 작은 동안
    while stack and frequency[a[stack[-1]]] < frequency[a[i]]:
        result[stack.pop()] = a[i]  # 오등큰수로 변경

    stack.append(i)

print(" ".join(map(str, result)))
