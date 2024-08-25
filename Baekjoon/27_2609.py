# 백준 2609번 "최대공약수와 최소공배수"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 부분 참고
# 이해도 : 높음 (유클리드 호제법, 문법에 대한 추가 이해 필요)
# 소요 시간 : 학습목적 (측정하지 않음)


#최대공약수(Greatest Common Divisor) 구하기 (유클리드 호제법)
def GCD(x,y):
    while(y): #y가 참일 동안 = 자연수일 때 =   a%b!=0
        x,y=y,x%y
    return x


#최소공배수(Lowest Common Multiple) 구하기
def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result


a, b = map(int, input().split())
print(GCD(a,b))
print(LCM(a,b))

