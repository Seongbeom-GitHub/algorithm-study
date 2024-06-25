# 백준 25178번
# 인기 투표 / 실버5 / 구현
# 풀이 : 답안 참고
# 이해도 : 문제 이해에 다소 시간소요
# 소요 시간 : 초과

from collections import Counter


# 문자의 길이 입력
n = int(input())

word1 = input()
word2 = input()
vowel = {'a', 'e', 'i', 'o', 'u'}

# 첫글자와 마지막 글자가 같은지 확인
if word1[0] != word2[0] or word1[-1] != word2[-1]:
    print("NO")
else:
    if Counter(word1) != Counter(word2) :
        print("NO")
    else : 
        # 자음이 같은지 체크
        a = [char for char in word1[1:-1] if char not in vowel]
        b = [char for char in word2[1:-1] if char not in vowel]
    
        if a == b:
            print("YES")
        else:
            print("NO")

