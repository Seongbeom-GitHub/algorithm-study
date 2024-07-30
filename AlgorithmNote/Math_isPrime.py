# 소수 판별 함수

import math

def isPrimeNumber(x):
    # 1은 소수가 아니므로 False 반환
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1) : # 2부터 x의 제곱근까지
        if x % i == 0:
            return False
    return True