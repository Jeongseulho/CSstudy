def starMaker(N):
    global sky
    if N == 1:
        return

    for i in range(N):
        for j in range(N):
            if (i // (N // 3)) % 3 == 1 and (j // (N // 3)) % 3 == 1:
                try:
                    for r in range(0, n, N):
                        for c in range(0, n, N):
                            sky[i + r][j + c] = ' '

                except IndexError:
                    pass

    return starMaker(N // 3)


N = int(input())
n = N

sky = [['*'] * N for _ in range(N)]
starMaker(N)
for i in range(N):
    print(''.join(sky[i]))