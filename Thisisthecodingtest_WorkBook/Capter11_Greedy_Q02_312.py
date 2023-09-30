# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 312p
# Q02. 곱하기 혹은 더하기
# 풀이일 : 2023-09-30
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분
# 소요 시간 : 32분 실패

# 1) 나의 틀린 풀이
# inputString = list(input())
# cal = []

# result = 0

# for i in inputString :
#     if i == '0' or i == '1' :
#         cal.append('+')
#     else :
#         cal.append('*')


# for i in (0, len(cal)) :
#     if i == 0 :
#         if cal[i] == '+' :
#             result = int(inputString[i]) + int(inputString[i+1])
#         else :
#             result = int(inputString[i]) * int(inputString[i+1])
#     else :
#         if cal[i] == '+' :
#             result += int(inputString[i+1])
#         else :
#             result *= int(inputString[i+1])

# print(result)

# 2) 모범 답안
data = input() # 데이터를 받아올 때 리스트 형태로 바꾸지 않아도 됨

result = int(data[0])  # 첫번째 수를 미리 result 값에 넣어둠

for i in range(1, len(data)) :
    num = int(data[i])   # 확인할 요소를 새로 만든 변수에 넣어둠 (코드를 간결하고 명확하게 표현)
    if num <= 1 or result <= 1 :     
        result += num
    else :
        result *= num

print(result)
