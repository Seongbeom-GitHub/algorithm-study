# 백준 17087번 "숨바꼭질 6"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 부분참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)


"""
< Comment >
1. reduce의 사용방법 숙지
2. math 라이브러리의 gcd 사용
"""

import math
from functools import reduce


# 여러 수의 최대 공약수 구하기
def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)


n, s = map(int, input().split())
brotherLocation = list(map(int, input().split()))

absList = []

for location in brotherLocation:
    absList.append(abs(location - s))

print(gcd_multiple(absList))
