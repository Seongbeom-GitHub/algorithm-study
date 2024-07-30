# 백준 1978번 "소수 찾기"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 높음 (소수 판별 알고리즘에 대해 학습함)
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

# n = int(input())
input_list = map(int, input().split())

primeCount = 0

for each in input_list:
    if isPrimeNumber(each):
        primeCount += 1

print(primeCount)
