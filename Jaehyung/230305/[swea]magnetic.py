for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        check = False
        for j in range(N):
            if data[j][i] == 1:
                check = True
            if check and data[j][i] == 2:
                cnt += 1
                check = False

    print(f'#{tc} {cnt}')