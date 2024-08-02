# 백준 2004번 "조합 0의 개수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고 (이해 안됨)
# 이해도 : 낮음
# 소요 시간 : 학습목적 (측정하지 않음)

import sys


def countnum(N, num):
    count = 0
    div = num
    while N >= div:
        count += N // div
        div *= num
    return count


n, m = map(int, sys.stdin.readline().split())
print(
    min(
        countnum(n, 5) - countnum(m, 5) - countnum(n - m, 5),
        countnum(n, 2) - countnum(m, 2) - countnum(n - m, 2),
    )
)
