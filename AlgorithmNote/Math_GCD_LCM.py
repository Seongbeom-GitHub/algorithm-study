
#최대공약수(Greatest Common Divisor) 구하기 (유클리드 호제법)
def GCD(x,y):
    while(y): #y가 참일 동안 = 자연수일 때 =   a%b!=0
        x, y = y, x % y
    return x

print(GCD(10,12))  #2



#최소공배수(Lowest Common Multiple) 구하기
def LCM(x,y):
    result = (x * y) // GCD(x,y)
    return result

print(LCM(10,12))   #60