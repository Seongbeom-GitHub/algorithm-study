# 백준 10809번 "알파벳 찾기"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 완벽 
# 소요 시간 : 학습목적 (측정하지 않음)

appearance = [-1] * 26

inputStr = input()

for i in range(len(inputStr)) :
    
    index = ord(inputStr[i]) - ord('a')

    if appearance[index] < 0 :
        appearance[index] = i
    
print(' '.join(map(str, appearance)))