# 백준 11005번 "진법 변환2"
# 문제 분류 : 알고리즘 기초 1/2
# 풀이 : 답안참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)

def convert_n(n, b):
    if n == 0:
        return '0'  # N이 0일 경우 '0'을 문자열로 반환

    digits = [] 
    while n > 0:
        temp = n % b
        if temp >= 10:
            digits.append(chr(temp - 10 + ord('A')))  # 알파벳으로 변환
        else:
            digits.append(str(temp))  # 숫자를 문자열로 변환
        n //= b

    return ''.join(reversed(digits))  # 뒤집어서 문자열로 결합

# 입력 받기
n, b = map(int, input().split())

# 결과 출력
result = convert_n(n, b)
print(result)
