# 백준 17103번 "골드바흐 파티션"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 부분참고
# 이해도 : 중간
# 소요 시간 : 학습목적 (측정하지 않음)

MAX_N = 1000001

# 소수 판별을 위한 리스트 생성
sosu = [True] * MAX_N
sosu[0] = sosu[1] = False  # 0과 1은 소수가 아님

# 에라토스테네스의 체
for i in range(2, int(MAX_N ** 0.5) + 1):
    if sosu[i]:
        for k in range(i * 2, MAX_N, i):
            sosu[k] = False

# 소수 리스트 생성
primes = [i for i in range(MAX_N) if sosu[i]]
prime_set = set(primes)  # 소수를 집합으로 변환하여 빠른 검색을 가능하게 함

t = int(input())    
result = []

for _ in range(t):
    n = int(input())
    countGoldbachPartition = 0

    # 소수 리스트를 이용하여 두 소수의 합이 N이 되는 경우를 찾음
    for prime in primes:
        if prime > n // 2:  # N/2보다 큰 소수는 필요 없음
            break
        if (n - prime) in prime_set:  # N - prime이 소수인지 확인
            countGoldbachPartition += 1

    result.append(countGoldbachPartition)

# 결과 출력
for res in result:
    print(res)
