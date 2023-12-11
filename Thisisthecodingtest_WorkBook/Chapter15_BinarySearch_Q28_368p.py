# "이것이 코딩 테스트다" / 챕터15 / Binary Search / 368p
# Q28. 고정점 찾기
# 풀이일 : 2023-12-11
# 난이도 : 1.5/3.0 
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 20분
# 소요 시간 : 
# 문제 출처 : Amazon 인터뷰

# 1) 나의 풀이 (시간초과)
# n = int(input())
# data = list(map(int, input().split()))

# for i in range(len(data)) :
#     if i == data[i] :
#         print(i)
#         break

# 2) 모범답안 (이진탐색활용)
def binary_serach(array,start, end) :
    if start > end :
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == mid :
        return mid
    
    # (중간점의 값 > 찾고자 하는 값) 왼쪽 확인
    elif array[mid] > mid :
        return binary_serach(array, start, mid - 1)
    
    # (중간점의 값 < 찾고자 하는 값) 오른쪽 확인
    else :
        return binary_serach(array, mid + 1, end)
    
n = int(input())    
array = list(map(int, input().split()))

index = binary_serach(array, 0, n-1)

if index == None :
    print(-1)
else :
    print(index)

