# 한 지점 기준으로 8x8 이동시키고 색깔 칠해지는 기준 틀리면 카운트.
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]


min_count = 70
for i in range(N):
    for j in range(M):
        # i와 j를 8번 하나씩 옮길건데 범위가 넘어가면 안됨.
        # 범위가 넘어가는 경우가 있는 지 확인 먼저
        if i+7 < N and j+7 < M:
            count = 0
            for k in range(8):
                for a in range(8):
                    ci = i + k
                    cj = j + a
                    # 색깔 검사해야 함
                    # 오른쪽과 아래의 색깔이 달라야 함
                    # 일단은 범위 넘지 않도록 해야 함
                    if ci + 1 < N and cj + 1 < M:
                        if data[ci][cj] == data[ci+1][cj] and data[ci][cj] == data[ci][cj+1]:
                            count += 1
            if count < min_count:
                min_count = count

print(min_count)


