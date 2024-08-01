# 백준 6588번 "골드바흐의 추측"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 낮음 (애매함)
# 소요 시간 : 학습목적 (측정하지 않음)


import sys

# 소수 판별을 위한 리스트 생성
sosu = [True] * 1000001
sosu[0] = sosu[1] = False  # 0과 1은 소수가 아님

# 에라토스테네스의 체
for i in range(2, int(1000001 ** 0.5) + 1):
    if sosu[i]:
        for k in range(i * 2, 1000001, i):
            sosu[k] = False

# 소수 리스트 생성
primes = [i for i in range(1000001) if sosu[i]]
prime_set = set(primes)  # 소수를 집합으로 변환하여 빠른 검색을 가능하게 함

results = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    found = False
    for i in primes:
        if i > n // 2:  # 짝수 n에 대해 i가 n의 절반을 넘으면 중지
            break
        if (n - i) in prime_set:  # n - i가 소수인지 확인
            results.append(f"{n} = {i} + {n - i}")
            found = True
            break

    if not found:
        results.append("Goldbach's conjecture is wrong.")

# 모든 결과를 한 번에 출력
for result in results:
    print(result)
