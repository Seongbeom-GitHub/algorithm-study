# 다이나믹프로그래밍 / 피보나치 / 재귀적 / Top-Down

# 한번 계산된 결과를 Memoization 하기 위한 초기화
d = [0] * 100

# Fibonacci Function
def fibo(x) :

    # 종료 조건(1 or 2일 때 1을 반환)
    if x == 1 or x == 2 : return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0 : return d[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)

    return d[x]

print(fibo(99))
