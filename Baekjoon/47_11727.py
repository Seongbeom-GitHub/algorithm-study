# 백준 11727번 "2*n 타일링 2"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 부분참고 (점화식 구상에 어려움)
# 이해도 : 높음 
# 소요 시간 : 학습목적 (측정하지 않음)

'''
Tip)
채울 수 있는 모양을 기존의 것에서 변화해서
가짓 수가 어떻게 늘어가는지 확인하여 점화식을 세운다.
'''


n = int(input())

if n < 1 :
    print()
else :
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2 :
        dp[2] = 3

    for i in range(3, n + 1) :
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    print(dp[n] % 10007)