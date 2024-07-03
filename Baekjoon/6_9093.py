# 백준 9093번 "단어뒤집기"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 상
# 소요 시간 : 학습목적 (측정하지 않음)

# 1. 초기 구상
t = int(input())
sentences = []

for _ in range(t) :
    sentences.append(input())

for sentence in sentences :
    words = sentence.split()

    for i, word in enumerate(words) :
        if i == len(words) - 1:
            print(word[::-1], end='')
        else:
            print(word[::-1], end=' ')
        
    print()


# 2. 코드 간단히
t = int(input())
sentences = [input() for _ in range(t)]

for sentence in sentences:
    words = sentence.split()
    reversed_words = ' '.join(word[::-1] for word in words) # join과 리스트컴프리헨션 이용
    print(reversed_words)


# 3. 이외에 스택이나 반복문을 사용하는 방법도 있음