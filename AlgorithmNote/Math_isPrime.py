# 소수 판별 함수

import math

def is_prime_number(x) :
    for i in range(2, int(math.sqrt(x)) + 1) : # 2부터 x의 제곱근까지
        if x % i == 0 :
            return False
        
    return True

