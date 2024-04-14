# 백준 1021번
# 회전하는 큐 / 실버3
# 풀이 : 답안 참고
# 이해도 : 중간 (로직을 코드화 하는 과정에서 어려움이 있었음)
# 소요 시간 : -

from collections import deque
import sys
input = sys.stdin.readline

# 큐의 크기, 뽑는 개수 입력
m, n = map(int, input().split())
# 뽑는 순서를 담는 배열
targets = list(map(int, input().split()))

# 큐 초기화
q = deque([i for i in range(1, m+1)])

count = 0
for target in targets :
        
    while True :
        if target == q[0] :
            q.popleft()
            break
        
        if q.index(target) <= len(q) // 2 :
            while target != q[0] :
                q.append(q.popleft())
                count += 1
        else :
            while target != q[0] :
                q.appendleft(q.pop())
                count += 1
        
print(count)

