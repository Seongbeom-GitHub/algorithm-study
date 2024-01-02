# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 315p
# Q05. 볼링공 고르기
# 풀이일 : 2023-10-03
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분

# 1) 나의 풀이 (성공)
# n, m = input().split()

# ball = list(map(int, input().split()))

# result = 0

# for i in range(0, len(ball) -1) :
#     for j in range(i+1, len(ball)) :
#         if ball[i] != ball[j] :
#             result += 1
# print(result)


# 2) 모범답안
n, m = map(int, input().split())
data = list(map, (int, input().split()))

# 무게별 공의 개수를 담는 배열 선언
array = [0] * 11

# 무게별 공의 개수 증가 
for x in data :
    array[x] += 1

# 결과값을 담을 변수
result = 0

# 1부터 마지막 무게까지
for i in range(1, m + 1) :
    n -= array[i]           # 전체개수 - i무게의 공의 개수
    result += array[i] * n  # i무게의 공의 개수 * 남은 공의 개수 = 증가

print(result)