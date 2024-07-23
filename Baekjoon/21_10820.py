# 백준 10820번 "문자열 분석"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상 (내장함수 사용에 미숙했음 / rstrip, islower, 등)
# 소요 시간 : 학습목적 (측정하지 않음)

import sys

result = []  # 결과를 저장할 리스트

while True:
    # 반복문에서의 input은 readline() 사용
    # readline을 사용해 한줄씩 입력 받기
    line = sys.stdin.readline().rstrip('\n') # rstrip()을 이용해 개행문자 제거

    if not line:
        break

    lower, upper, num, space = 0, 0, 0, 0

    for each in line:
        if each.islower(): # 소문자 검사
            lower += 1
        elif each.isupper(): # 대문자 검사
            upper += 1
        elif each.isdigit(): # 숫자 검사
            num += 1
        elif each.isspace(): # 공백 검사
            space += 1

    # str.format()을 사용하여 결과를 리스트에 추가
    result.append("{} {} {} {}".format(lower, upper, num, space))

# 모든 결과를 한 번에 출력
print("\n".join(result))
