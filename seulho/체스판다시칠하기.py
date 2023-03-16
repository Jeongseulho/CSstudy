N, M = map(int, input().split())
arr = [input() for _ in range(N)]
minCnt = 64
for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        start_color1 = 'B'
        start_color2 = 'W'
        for k in range(i, i + 8):
            for m in range(j, j + 8):
                cur_color = arr[k][m]

                if k % 2:

                    if m % 2 and cur_color != start_color1:
                        cnt1 += 1
                    elif not m % 2 and cur_color == start_color1:
                        cnt1 += 1

                    if m % 2 and cur_color != start_color2:
                        cnt2 += 1
                    elif not m % 2 and cur_color == start_color2:
                        cnt2 += 1

                else:
                    if not m % 2 and cur_color != start_color1:
                        cnt1 += 1
                    elif m % 2 and cur_color == start_color1:
                        cnt1 += 1

                    if not m % 2 and cur_color != start_color2:
                        cnt2 += 1
                    elif m % 2 and cur_color == start_color2:
                        cnt2 += 1

        if cnt2 < minCnt:
            minCnt = cnt2
        if cnt1 < minCnt:
            minCnt = cnt1

print(minCnt)
