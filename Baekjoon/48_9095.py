# 백준 9095번 "1, 2, 3 더하기"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 부분참고 (점화식 구상에 어려움)
# 이해도 : 높음 
# 소요 시간 : 학습목적 (측정하지 않음)

'''
1, 2, 3 구성의 계산식에서 규칙성을 찾고 정확한 점화식을 찾아내야 한다.
'''

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    
    # dp 배열 초기화 및 기본 값 설정
    dp = [0] * 11  # n은 11보다 작으므로 0부터 10까지의 크기로 초기화
    dp[1], dp[2], dp[3] = 1, 2, 4  # 초기값 설정

    # n이 4 이상일 경우 동적 계획법을 사용하여 계산
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
    results.append(dp[n])

# 결과 출력
print('\n'.join(map(str, results)))
