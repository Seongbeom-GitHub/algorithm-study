# 백준 11576번 "Base Conversion"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 중간 (다소 혼동되는 부분 있음)
# 소요 시간 : 학습목적 (측정하지 않음)

a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
arr.reverse()

deciaml = 0 # 10진수 변환값을 담을 변수
result = []


# a진법의 수를 10진수로 변환
for i in range(len(arr)) :
    deciaml += arr[i] * (a ** i)

# 10진수를 b진법으로 변환
while deciaml // b : # 몫이 0이 될때까지 반복해서 나누기 (0은 False)
    result.append(deciaml % b) # 나머지 값을 저장
    deciaml //= b
result.append(deciaml) # 마지막 몫을 배열에 추가

result.reverse()
print(' '.join(map(str, result)))
