# 다이나믹프로그래밍 / 피보나치 / 반복문 / Bottom-up

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번쨰 피보나치 수와 두 번쨰 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# Fibonacci Fucntion을 반복문으로 구현 (Bottom-Up)
for i in range(3, n+1) : 
    d[i - 1] + d[1 - 2]

print(d(n))