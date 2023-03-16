N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 64
for i in range(0, N - 7):
    for j in range(0, M - 7):
        cnt_w = cnt_b = 0   # 처음으로 본 칸에 w가 칠해져있어야하나, b가 칠해져있어야 하나.
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                # 홀수행 + 홀수열, 짝수행 + 짝수열 -> 짝수
                # 둘이 다를 경우에는 홀수
                # 행값과 열값을 더해서 홀수가 나오는 칸, 짝수가 나오는 칸끼리 체스판 모양
                if (r + c) % 2:
                    if board[r][c] == 'W':  # 홀수가 나오는 칸에는 W가 칠해져있다 가정
                        cnt_w += 1
                    if board[r][c] == 'B':  # 홀수가 나오는 칸에는 B가 칠해져있다 가정
                        cnt_b += 1
                else:
                    if board[r][c] == 'B':  # 짝수가 나오는 칸에는 B가 칠해져 있어야 할 것.
                        cnt_w += 1
                    if board[r][c] == 'W':  # 짝수가 나오는 칸에는 W가 칠해져 있어야 할 것.
                        cnt_b += 1

        if ans > cnt_b:
            ans = cnt_b
        if ans > cnt_w:
            ans = cnt_w

print(ans)