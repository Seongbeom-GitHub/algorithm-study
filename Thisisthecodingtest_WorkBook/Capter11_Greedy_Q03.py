# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 313p
# Q03. 문자열 뒤집기
# 풀이일 : 2023-09-30
# 난이도 : 하
# 시간 제한 : 2초
# 메모리 제한 128MB
# 제한 시간 : 20분
# 소요 시간 : 22분 (실패)

# 1) 나의 풀이(수정 / 바르게 출력됨)
data = list(input())

zeroGroup = 0
oneGroup = 0

if data[0] == '0' : 
    zeroGroup += 1
elif data[1] == '1' : 
    oneGroup += 1

for i in range(len(data)-1) :
    num = data[i]
    if num == data[i+1] :
        continue
    elif data[i+1] == '0' :
        zeroGroup += 1
    elif data[i+1] == '1' :
        oneGroup += 1

print(min(zeroGroup, oneGroup))

# 2) 모범 답안
# data = input()
# count0 = 0
# count1 = 0

# if data[0] == '1' :
#     count0 += 1
# else :
#     count1 += 1

# for i in range(len(data) - 1) :
#     if data[i] != data[i+1] :
#         if data[i+1] == '1' :
#             count0 += 1
#         else :
#             count1 += 1

# print(min(count0, count1))