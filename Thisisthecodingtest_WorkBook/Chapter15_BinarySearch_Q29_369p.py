# "이것이 코딩 테스트다" / 챕터15 / Binary Search / 369p
# Q29. 공유기 설치
# 풀이일 : 2023-12-11
# 난이도 : 2.0/3.0 
# 시간 제한 : 2초
# 메모리 제한 128MB
# 풀이 제한 시간 : 50분
# 소요 시간 : 
# 문제 출처 : https://acmicpc.net/problem/2110


# 집의 개수(N)와 공유기의 개수 (C)를 입력
n, c = list(map(int, input().split()))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n) :
    array.append(int(input()))
array.sort()

start = array[1] - array[0] # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값
result = 0

while (start <= end) :
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = array[0]
    count = 1

    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n) :
        if array[i] >= value + mid :
            value = array[i]
            count += 1
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)
