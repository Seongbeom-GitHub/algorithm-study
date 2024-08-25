# 백준 1929번 "소수 구하기"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 직접풀이
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)

import math

def isPrimeNumber(x):
    # 1은 소수가 아니므로 False 반환
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

m, n = map(int, input().split())
result = []

for i in range(m, n + 1) :
    if isPrimeNumber(i) :
        result.append(i)
    
for each in result :
    print(each)