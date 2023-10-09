# "이것이 코딩 테스트다" / 챕터12 / 구현 / 325p
# Q10. 자물쇠와 열쇠
# 풀이일 : 2023-10-07
# 난이도 : 1.5/3.0
# 시간 제한 : 1초
# 메모리 제한 128MB
# 풀이 제한 시간 : 40분
# 소요 시간 : 
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 1) 나의 풀이

# 2) 모범답안

# 시계방향 90도 회전
def rotate_matrix_by_90_degree(a) :
    n = len(a)      # 행의 길이
    m = len(a[0])   # 열의 길이
    result = [[0] * n for _ in range(m)]    # 결과 리스트
        
    for i in range(n) :
        for j in range(m) :
            result[j][n - i - 1] = a[i][j]

    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1 :
                return False
    return True

def solution(key, lock) :
    n = len(lock)       # 자물쇠의 행 크기
    m = len(lock[0])    # 자물쇠의 열 크기

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n) :
        for j in range(n) :
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해 확인
    for rotation in range(4) :
        key = rotate_matrix_by_90_degree(key) # 열쇠 회전
        

        for x in range(n * 2) :
            for y in range(n * 2) :

                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] += key[i][j]
                
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True :
                    return True
                
                # 자물쇠에서 열쇠를 다시 뺴기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] -= key[i][j]

    return False