# 백준 9613번 "GCD 합"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 부분참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)


"""
< Comment >
1. 조합 라이브러리 사용함
2. GCD의 값은 math.gcd를 이용할 수도 있음
"""

from itertools import combinations


# 최대공약수(Greatest Common Divisor) 구하기 (유클리드 호제법)
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

t = int(input())
result = []

for _ in range(t):
    inputList = list(map(int, input().split()))

    n = inputList[0]  # 첫 번째 요소는 수의 개수
    numbers = inputList[1:]  # 나머지는 실제 수들

    sum_gcd = 0
    combi = combinations(numbers, 2)

    for each in combi:
        sum_gcd += GCD(each[0], each[1])

    result.append(sum_gcd)

for i in result:
    print(i)
