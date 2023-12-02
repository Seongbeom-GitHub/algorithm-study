# "이것이 코딩 테스트다" / 챕터14 / Sorting / 359p
# Q23. 국영수
# 풀이일 : 2023-12-02
# 난이도 : 1.0/3.0 
# 시간 제한 : 1초
# 메모리 제한 256MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 
# https://acmicpc.net/problem/10825

n = int(input())

student = []

for i in range(n) :
    student.append(input().split())

student.sort(key = lambda x : ( -int(x[1]), int(x[2]), -int(x[3]), x[0] ) )

for s in student :
    print(s[0])