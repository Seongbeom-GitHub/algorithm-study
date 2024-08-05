# 백준 2089번 "-2 진수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 낮음 (애매함 / -2진수 변환과정이 다소 어려움)
# 소요 시간 : 학습목적 (측정하지 않음)

n = int(input())
result = ""

if n == 0 :
    result += "0"
    print(result)
else :
    while n :
        if n % (-2) :
            result = '1' + result
            n = n // -2 + 1
        else :
            result = '0' + result
            n = n // -2
    print(result)


