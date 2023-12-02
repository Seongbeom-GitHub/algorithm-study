# "이것이 코딩 테스트다" / 챕터14 / Sorting / 360p
# Q24. 안테나
# 풀이일 : 2023-12-02
# 난이도 : 1.0/3.0 
# 시간 제한 : 1초
# 메모리 제한 256MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 
# https://acmicpc.net/problem/18310

# 1) 나의 풀이 (시간초과)
# n = int(input())
# pos = list(map(int, input().split()))
# sub_list = []

# min_value = 1e9

# for i in pos :
#     sub = 0
#     for j in pos :
#         sub += abs(i - j)
#     sub_list.append(sub)
#     min_value = min(min_value, sub)

# for x in range(len(sub_list)) :
#     if sub_list[x] == min_value :
#         print(pos[x])
#         break



# 2) 모범 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])