T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for dr, dc in [(1, 0), (0, 1), (1, -1), (1, 1)]:  # 하 우 좌하 우하
                    nr = dr + i
                    nc = dc + j
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        for _ in range(3):
                            nr += dr
                            nc += dc
                            if not(0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o'):
                                break
                        else:
                            result = True
    if result:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')