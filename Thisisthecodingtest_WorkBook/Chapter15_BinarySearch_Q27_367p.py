# "이것이 코딩 테스트다" / 챕터15 / Binary Search / 367p
# Q27. 정렬된 배열에서 특정 수의 개수 구하기
# 풀이일 : 2023-12-11
# 난이도 : 2.0/3.0 
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 30분
# 소요 시간 : 
# 문제 출처 : Zoho 인터뷰

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))


count = bisect_right(data, x) - bisect_left(data, x)

if count == 0 :
    print(-1)
else :
    print(count)