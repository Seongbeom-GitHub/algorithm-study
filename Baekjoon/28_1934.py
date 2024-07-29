# 백준 1934번 "최소공배수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 직접풀이
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)


def GCD(x, y) :
    while(y) :
        x, y = y, x % y
    return x

def LCM(x, y) :
    result = (x * y) // GCD(x, y)
    return result

t = int(input())
result = []

for _ in range(t) :
    a, b = map(int, input().split())
    result.append(LCM(a,b))

for each in result :
    print(each)