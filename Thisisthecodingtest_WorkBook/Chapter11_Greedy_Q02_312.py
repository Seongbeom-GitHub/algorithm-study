# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 312p
# Q02. 곱하기 혹은 더하기
# 풀이일 : 2023-09-30
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분

data = input() # 데이터를 받아올 때 리스트 형태로 바꾸지 않아도 됨

result = int(data[0])  # 첫번째 수를 미리 result 값에 넣음

for i in range(1, len(data)) :
    num = int(data[i])  
    if num <= 1 or result <= 1 :     
        result += num
    else :
        result *= num

print(result)
