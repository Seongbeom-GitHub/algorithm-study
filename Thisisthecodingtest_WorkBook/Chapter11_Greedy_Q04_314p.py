# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 314p
# Q04. 만들 수 없는 금액
# 풀이일 : 2023-10-01
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
    # 더해온 수 보다 다음 수가 더 크다면 브레이크
    if target < x : 
        break
    target += x

print(target)

