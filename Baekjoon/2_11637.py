# 백준 11637번
# 인기 투표 / 실버5 / 구현
# 풀이 : 부분 참고
# 이해도 : 중 ()
# 소요 시간 : 40분(성공)


# 테스트 케이스 개수 입력
t = int(input())
# 결과를 저장할 리스트
results = []

for _ in range(t) :
    
    # 후보자 수
    n = int(input())
    # 후보자들의 득표수를 배열에 담음
    candidates = [int(input()) for _ in range(n)]
    # 최다 득표값
    candiMax = max(candidates)

    flag = 0
    total = 0
    for candidate in candidates :
        if candidate == candiMax :
            flag += 1
        else :
            total += candidate
    if flag > 1 :
        results.append("no winner")
        continue
    else :
        r = candidates.index(candiMax) + 1
        if candiMax > total :
            results.append("majority winner " + str(r))
        else :
            results.append("minority winner " + str(r))


# 입력 받는 과정이 모두 끝난 후 결과 출력
for result in results:
    print(result)
    









