T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    result = 'NO'
    # 우 하 우하 좌하 만 필요
    dr = [1, 0, 1, -1]
    dc = [0, 1, 1, 1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    si = i
                    sj = j
                    cnt = 0
                    while 0 <= si < N and 0 <= sj < N and arr[si][sj] == 'o':
                        cnt += 1
                        si = si + dr[d]
                        sj = sj + dc[d]
                    if cnt >= 5:
                        result = 'YES'


    print(f'#{tc} {result}')