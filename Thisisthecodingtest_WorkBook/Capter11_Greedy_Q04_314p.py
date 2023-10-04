# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 314p
# Q04. 만들 수 없는 금액
# 풀이일 : 2023-10-01
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분
# 소요 시간 : 22분 포기

# 1) 나의 풀이
# coin = list(map(int,input().split()))

# print(coin)

# while True :
#     result = 1

#     # 코인 1개
#     for a in coin :
#         if a == result :
#             result = a
#             break

#     # 2개 이상
#     for b in coin :
#         for i in (b+1, coin)

# 2) 모범 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
    if target < x : 
        break
    target += x

print(target)

