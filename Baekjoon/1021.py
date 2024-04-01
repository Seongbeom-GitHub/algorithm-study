# 백준 1021번
# 회전하는 큐 / 실버3


from collections import deque

# 큐의 크기, 뽑는 개수 입력
m, n = map(int, input().split())
# 뽑는 순서를 담는 배열
targets = list(map(int, input().split()))

# 큐 초기화
q = deque([i for i in range(1, m+1)])

count = 0
for target in targets :
        
    while true :
        if target == q[0] :
            q.popleft()
            break
        
        if q.index(target) <= len(q) // 2 :
            while target != q[0] :
                



    # 123456 78910
