# "이것이 코딩 테스트다" / 챕터12 / 구현 / 321p
# Q07. 럭키 스트레이트
# 풀이일 : 2023-10-06
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 256MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 20분 (성공)


# 1) 나의 풀이 (성공)
# n = input()


# left = n[: int(len(n)/2 - 1)]
# right = n[int(len(n)/2) : len(n)]


# l = 0
# r = 0

# for i in range(0, int(len(n)/2)) :
#     l += int(n[i])
# for j in range(int(len(n)/2 + 1), len(n)) :
#     r += int(n[i])

# print("LUCKY" if l == r else "READY")

# 2) 모범답안
n = input()
length = len(n)
summary = 0

for i in range(length //2) :
    summary += int(n(i))

for i in range(length // 2, length) :
    summary -= int(n[i])

if summary == 0 :
    print("LUCKY")
else :
    print("READY")