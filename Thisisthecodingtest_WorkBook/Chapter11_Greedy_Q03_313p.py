# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 313p
# Q03. 문자열 뒤집기
# 풀이일 : 2023-09-30
# 난이도 : 하
# 시간 제한 : 2초
# 메모리 제한 128MB
# 제한 시간 : 20분

data = input()
count0 = 0 # 0으로 이어진 그룹 수
count1 = 0 # 1로 이어진 그룹 수

# 첫번째 문자를 그룹에 담기
if data[0] == '1' :
    count0 += 1
else :
    count1 += 1

for i in range(len(data) - 1) :
    # 현재와 다음 수를 비교하여 같지 않으면 그룹수를 카운트
    if data[i] != data[i+1] :
        if data[i+1] == '0' :
            count0 += 1
        else :
            count1 += 1

# 더 적은 그룹을 가지고 있는 수 출력
print(min(count0, count1))