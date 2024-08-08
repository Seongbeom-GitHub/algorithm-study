# 백준 11653번 "소인수분해"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 부분참고
# 이해도 : 높음
# 소요 시간 : (측정하지 않음)

n = int(input())    
result = [] 

if n <= 1 :
    print()
else :
    d = 2
    while n > 1 : # 몫이 1일때 반복 종료
        if n % d == 0 :
            result.append(d)
            n //= d
        else :
            d += 1

for each in result :
    print(each)