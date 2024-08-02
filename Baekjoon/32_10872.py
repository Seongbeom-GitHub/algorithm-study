# 백준 10872번 "팩토리얼"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 부분참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)

n = int(input())

def myFactorial(n) :
    a = 1
    for i in range(1, n + 1) :
        a *= i
    return a

print(myFactorial(n))

# import math
# math.factorial(n) 