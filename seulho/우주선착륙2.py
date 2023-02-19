di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [['?'] * (M + 2)] + [['?'] + list(map(int, input().split())) + ['?']
                                for _ in range(N)] + [['?'] * (M + 2)]
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            center = grid[i][j]
            lowerPlace = 0
            for dir in range(8):
                adjI = i + di[dir]
                adjJ = j + dj[dir]
                adjacentPlace = grid[adjI][adjJ]
                if adjacentPlace != '?' and adjacentPlace < center:
                    lowerPlace += 1
            if lowerPlace >= 4:
                cnt += 1

    print(f'#{test_case} {cnt}')
