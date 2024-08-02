# 백준 1676번 "팩토리얼 0의 개수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 부분참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)

n = int(input())

def myFactorial(n) :
    result = 1
    for i in range(n, 0, -1) :
        result *= i
    return result


myStr = str(myFactorial(n))

zeroCount = 0

for each in reversed(myStr) :
    if each != '0' :
        break
    else :
        zeroCount += 1

print(zeroCount)