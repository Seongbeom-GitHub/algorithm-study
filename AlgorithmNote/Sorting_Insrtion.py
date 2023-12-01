# 삽입정렬 (Insertion Sort)
# 아이디어 : 앞에서 부터 하나씩 확인, 좌측부터 점검하여 적절한 위치에 삽입
# 특징 : 거의 정렬된 데이터 정렬에 효율적

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) : # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1] : # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else : # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
