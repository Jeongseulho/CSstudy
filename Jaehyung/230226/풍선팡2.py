T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    maxflo = 0
    # 전부 델타로 확인하고 합 구해서 최대값만 저장
    for i in range(N):
        for j in range(M):
            flo = data[i][j]
            for k in [(0,-1),(0,1),(-1,0),(1,0)]: # 좌 우 상 하
                ni = i + k[0]
                nj = j + k[1]
                if 0 <= ni < N and 0 <= nj < M:
                    flo += data[ni][nj]
            if flo > maxflo:
                maxflo = flo
    print(f'#{tc} {maxflo}')