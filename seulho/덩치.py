N = int(input())
people = [0] * N  # 사람의 키, 몸무게 정보 리스트
result = [0] * N  # 해당 순위 리스트

# 입력 받는 부분
for i in range(N):
    info = list(map(int, input().split()))
    people[i] = info


# people을 돌면서 모두 비교
for i in range(N):
    rank = 1
    cur_w = people[i][0]
    cur_h = people[i][1]

    for j in range(N):
        other_w = people[j][0]
        other_h = people[j][1]
        if cur_w < other_w and cur_h < other_h:
            rank += 1

    result[i] = rank

print(*result)
