# 백준 11655번 "ROT13"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

s = input()
result = []

for each in s:
    # 대문자인 경우
    if each.isupper():
        result.append(chr(  (ord(each) - ord('A') + 13) % 26 + ord('A')  ))
    # 소문자인 경우
    elif each.islower():
        result.append(chr((ord(each) - ord('a') + 13) % 26 + ord('a')))
    else:
        result.append(each)

print(''.join(result))
