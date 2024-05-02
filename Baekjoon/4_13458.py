# 백준 13458번
# 시험 감독 / 브론즈2 / 삼성SW역량테스트
# 풀이 : 풀이완료
# 이해도 : 상 (문제이해 O, 구조 생각에 시간소모)
# 소요 시간 : 약 30분


n = int(input()) # 전체 시험장의 수
a = list(map(int, input().split())) # 각 시험장의 인원수
b, c = map(int, input().split()) # 총감독관 감시인원, 부감독관 감시인원
result = 0 # 필요한 감독관 수


for i in  a :
    x = i
    
    if x <= b :
        result += 1
    elif (x - b) % c == 0 :
        result += (x - b) // c + 1
    else : 
        result += (x - b) // c + 2
    


print(int(result))




