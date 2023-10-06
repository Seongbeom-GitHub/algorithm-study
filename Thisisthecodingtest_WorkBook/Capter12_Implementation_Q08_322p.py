# "이것이 코딩 테스트다" / 챕터12 / 구현 / 322p
# Q08. 
# 풀이일 : 2023-10-06
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 12분 (성공)

# 1) 나의 풀이
# s = input()

# stringSum = []
# digitSum = 0

# for a in s :
#     if a.isdigit() == True :
#         digitSum += int(a)
#     else :
#         stringSum.append(a)

# stringSum.sort()
# for i in stringSum :
#     print(i, end="")
# print(digitSum)

# 2) 모범 답안
data = input()
result = []
value = 0

for x in data :
    if x.isalpha() :
        result.append(x)
    else :
        value += int(x)

result.sort()

if value != 0 :
    result.append(str(value))

print('', join(result))