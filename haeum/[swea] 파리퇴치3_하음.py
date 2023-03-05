T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            # 십자
            ans = board[i][j]
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = i + dr
                nc = j + dc
                cnt = 1
                while 0 <= nr < N and 0 <= nc < N and cnt < M:
                    ans += board[nr][nc]
                    nr += dr
                    nc += dc
                    cnt += 1
            mx = max(mx, ans)
            ans = board[i][j]

            # X
            for dr, dc in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
                nr = i + dr
                nc = j + dc
                cnt = 1
                while 0 <= nr < N and 0 <= nc < N and cnt < M:
                    ans += board[nr][nc]
                    nr += dr
                    nc += dc
                    cnt += 1
            mx = max(mx, ans)

    print(f'#{tc} {mx}')