# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 315p
# Q05. 볼링공 고르기
# 풀이일 : 2023-10-03
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분
# 소요 시간 : 15분 30초 (풀이 완료)

# import math
# import time
# start = time.time()
# end = time.time()
# print(f"{end - start : .5f} sec")


# 1) 나의 풀이
n, m = input().split()

ball = list(map(int, input().split()))

result = 0

for i in range(0, len(ball) -1) :
    for j in range(i+1, len(ball)) :
        if ball[i] != ball[j] :
            result += 1


print(result)


# 2) 모범답안
