# 백준 1158번 "요세푸스 문제"
# 문제 분류 : 알고리즘 기초 1/2 (자료구조)
# 풀이 : 성공
# 이해도 : 중 (%연산을 통한 회전 큐의 인덱스 접근에 대한 아이디어 구상이 어려웠음)
# 소요 시간 : 학습목적 (측정하지 않음)

def josephus(N, K) :
    index = 0
    result = []
    people = (list(range(1, N + 1)))

    while people :
        index = ( index + K -1 ) % len(people) # 다음으로 제거할 사람의 인덱스 계산 (%를 통한 회전 큐 기능)
        result.append(people.pop(index))

    return result

  
n, k = map(int, input().split())    

result = josephus(n, k)

print("<" + ", ".join(map(str, result)) + ">") # join은 문자열 함수이기 때문에 map으로 변환