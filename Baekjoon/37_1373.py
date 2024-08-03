# 백준 1373번 "2진수 8진수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 답안참고
# 이해도 : 높음
# 소요 시간 : 학습목적 (측정하지 않음)



# ----(풀이1) 내장 함수 이용

n = input()

# 2진수 -> 10진수 변환 
d = int(n,2)

# 10진수 -> 8진수 변환 
print(oct(d)[2:])




# ----(풀이2) 3자리씩 끊어서 변환

def binary_to_octal(binary_str):
    # 2진수 길이가 3의 배수가 될 때까지 왼쪽에 0 추가
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str

    octal_str = ''
    
    # 3자리씩 나누어 8진수로 변환
    for i in range(0, len(binary_str), 3):
        # 3자리 2진수를 10진수로 변환
        num = (int(binary_str[i]) * 4) + (int(binary_str[i + 1]) * 2) + (int(binary_str[i + 2]) * 1)
        octal_str += str(num)

    return octal_str


binary_input = input()
octal_output = binary_to_octal(binary_input)
print(octal_output)
