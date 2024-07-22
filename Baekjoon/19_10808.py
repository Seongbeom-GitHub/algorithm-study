# 백준 10808번 "알파벳 개수"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 완벽
# 소요 시간 : 학습목적 (측정하지 않음)

frequency = [0] * 26

inputStr = input()

for c in inputStr :
    frequency[ord(c) - ord('a')] += 1

print(' '.join(map(str, frequency)))