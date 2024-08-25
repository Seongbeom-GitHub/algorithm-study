# 백준 2004번 "조합 0의 개수"
# 문제 분류 : 알고리즘 기초 1/2 
# 풀이 : 답안참고 (이해 어려웠음)
# 이해도 : 낮음
# 소요 시간 : 학습목적 (측정하지 않음)


'''
1. 조합에 대한 이해
2. 0의 자리가 나오려면 2와 5의 인수 개수를 생각해야한다.
3. 조합의 계산식에서 인수의 차이 계산을 떠올려야한다. (n - m - (n - m))
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def count_2(N):
    if N < 2:
        return 0
    
    count = 0
    while N >= 2:
        count += N//2
        N = N//2
    return count

def count_5(N):
    if N < 5:
        return 0
    
    count = 0
    while N >= 5:
        count += N//5
        N //= 5
    return count

two_cnt = count_2(n) - count_2(n-m) - count_2(m)
five_cnt = count_5(n) - count_5(n-m) - count_5(m)
print(min(two_cnt, five_cnt))