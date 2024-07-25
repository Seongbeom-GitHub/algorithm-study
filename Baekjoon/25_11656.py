# 백준 11656번 "접미사 배열"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

s = input()
temp = []

# 모든 접미사를 생성
for i in range(len(s)):
    temp.append(s[i:])

# 정렬
result = sorted(temp)


for each in result:
    print(each)
