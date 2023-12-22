# (Other) 알고리즘 기타 테크닉
# 2차원 리스트 90, 180, 270도 회전

# 시계방향 90도 회전
def rotate_matrix_by_90_degree(a) :
    n = len(a)      # 행의 길이
    m = len(a[0])   # 열의 길이
    result = [[0] * n for _ in range(m)]    # 결과 리스트
        
    for i in range(n) :
        for j in range(m) :
            result[j][n - i - 1] = a[i][j]

    return result

# 시계방향 180도 회전
def rotate_matrix_by_180_degree(a) :
    n = len(a)
    m = len(a[0]) 
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[m-j-1][n-i-1] = a[i][j]

    return result

# 시계방향 270도 회전
def rotate_matriz_by_270_degree(a) :
    n = len(a) 
    m = len(a[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[m-j-1][i] = a[i][j]
            
    return result
