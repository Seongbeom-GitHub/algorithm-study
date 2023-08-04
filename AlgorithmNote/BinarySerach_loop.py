# 이진탐색 소스코드 구현 (반복문)

def binary_serach(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        
        # (중간점의 값 > 찾고자 하는 값) 왼쪽 확인
        elif array[mid] > target :
            end = mid - 1
        
        # (중간점의 값 < 찾고자 하는 값) 오른쪽 확인
        else :
            start = mid + 1

    return None




# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진탐색 수행 결과 출력
result = binary_serach(array, target, 0, n-1)
if result == None :
    print("원소가 존재하지 않습니다.")
else :
    # (+1은 몇번째에 있다는 기준으로 표현하기 위함임)
    print(result + 1)