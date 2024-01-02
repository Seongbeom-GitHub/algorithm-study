# "이것이 코딩 테스트다" / 챕터11 / 그리디 / 311p
# Q01. 모험가 길드
# 풀이일 : 2023-09-28
# 난이도 : 하
# 시간 제한 : 1초
# 메모리 제한 128MB
# 제한 시간 : 30분


n = int(input()) # 인원수
data = list(map(int, input().split()))      
data.sort() # 오름차순 정렬

result = 0   # 전체 그룹수
count = 0    # 현재 그룹에 포함된 인원수

# 23122
# 12223


for i in data :         # 낮은 공포도 순으로 꺼냄
    count += 1          # 현재 그룹의 인원수 증가
    if count >= i :     # 현재 그룹의 인원수 >= 꺼낸 인원의 공포도
        result += 1     # 전체 그룹수 증가
        count = 0       # 현재 그룹 인원수 초기화

print(result)