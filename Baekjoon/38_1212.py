# 백준 1212번 "8진수 2진수"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 부분참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)


n = input()

b = bin(int(n, 8))

print(b[2:])
