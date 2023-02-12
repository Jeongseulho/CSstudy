dj = [-1, 1, 0]
di = [0, 0, 1]
# 좌, 우, 하
T = 10
for test_case in range(1, T + 1):
    TC = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    startJList = []
    for i in range(100):
        if ladder[0][i] == 1:
            startJList.append(i)
    ans = 0

    for startJ in startJList:

        curJ = startJ
        curI = 0
        dir = 0

        while curI < 99:
            nextJ = curJ + dj[dir]
            nextI = curI + di[dir]
            if nextI < 0 or nextI > 99 or nextJ < 0 or nextJ > 99 or ladder[nextI][nextJ] == 0 \
                    or ladder[nextI][nextJ] == 'x':
                dir = (dir + 1) % 3

            else:
                ladder[curI][curJ] = 'x'
                curJ = nextJ
                curI = nextI
                dir = 0

        if ladder[curI][curJ] == 2:
            ans = startJ
            break

        for i in range(100):
            for j in range(100):
                if ladder[i][j] == 'x':
                    ladder[i][j] = 1

    print(f'#{test_case} {ans}')
