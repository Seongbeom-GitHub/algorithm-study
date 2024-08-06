# 백준 11005번 "진법 변환2"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 중간 (다소 혼동되는 부분 있음)
# 소요 시간 : 학습목적 (측정하지 않음)

def convert_to_decimal(x, b):
    # 숫자와 알파벳을 포함한 문자열 정의
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    decimal_value = 0
    length = len(x)
    
    for i in range(length):
        char = x[length - 1 - i]  # 뒤에서부터 읽기
        value = digits.index(char)  # 인덱스를 통해 값 얻기
        decimal_value += value * (b ** i)  # 각 자리수의 값 계산
    
    return decimal_value

# 입력 받기
x, b = input().split()
b = int(b)

# 결과 출력
result = convert_to_decimal(x, b)
print(result)
