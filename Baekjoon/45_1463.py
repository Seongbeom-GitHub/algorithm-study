# 백준 1463번 "1로 만들기"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 답안참고 (강의시청)
# 이해도 : 높음 
# 소요 시간 : 학습목적 (측정하지 않음)

'''
< 다이나믹 프로그래밍의 기초 문제 >
규칙성을 찾은 후, 초기값을 넣고 loop를 돌려 전체를 채워가는 방식
'''

n = int(input())    

dp = [0] * (n + 1)

for i in range(2, n + 1) :
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)


result = dp[n]
print(result)
