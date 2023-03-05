T = int(input())
# 파리 잡기
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우 우상 좌상 우하 좌하
    move = [(-1, 0), (1, 0), (-1, 0), (1, 0),
            (-1, 1), (-1, -1), (1, 1), (1, -1)]
    max_fly = 0
    for i in range(N):
        for j in range(N):
            fly_cnt = 0
            fly_cnt += arr[i][j]
            for dir in move:
                for k in range(1, M):
                    next_i, next_j = i + dir[0] * k, j + dir[1] * k
                    if 0 <= next_i < N and 0 <= next_j < N:
                        fly_cnt += arr[next_i][next_j]

            if fly_cnt > max_fly:
                max_fly = fly_cnt
    print(f"#{tc} {max_fly}")
#


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]  # 상, 우, 하, 좌

    for i in range(N):
        for j in range(N):
            sums = 0
            sums += arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nextr, nextc = i + dr[k] * l, j + dc[k] * l
                    if nextc < 0 or nextc >= N or nextr < 0 or nextr >= N:
                        break
                    sums += arr[nextr][nextc]
            if sums > result:
                result = sums

    dr2 = [1, -1, -1, 1]
    dc2 = [1, 1, -1, -1]  # 우하 우상 좌상 좌하

    for i in range(N):
        for j in range(N):
            sums = 0
            sums += arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nextr, nextc = i + dr2[k] * l, j + dc2[k] * l
                    if nextc < 0 or nextc >= N or nextr < 0 or nextr >= N:
                        break
                    sums += arr[nextr][nextc]
            if sums > result:
                result = sums

    print(f"#{tc} {result}")


lst = [[(-1, 0), (1, 0), (0, -1), (0, 1)],
       [(-1, -1), (-1, 1), (1, -1), (1, 1)]]

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # NxN 배열, 각 방향으로 M칸
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for si in range(N):
        for sj in range(N):
            for t in range(2):
                sm = arr[si][sj]
                for di, dj in lst[t]:
                    for m in range(1, M):
                        ni, nj = si + di * m, sj + dj * m
                        if 0 <= ni < N and 0 <= nj < N:
                            sm += arr[ni][nj]
                if sm > ans:
                    ans = sm

    print(f'#{test_case} {ans}')
