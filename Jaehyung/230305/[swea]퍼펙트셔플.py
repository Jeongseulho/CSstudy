T = int(input())
for tc in range(1, T+1):
    N = int(input())
    k = N
    if N % 2:
        N += 1
    data = list(input().split())
    print(f'#{tc}', end=' ')
    for i in range(N//2):
        print(data[i], end=' ')
        if i+N//2 < k:
            print(data[i+N//2], end=' ')
    print()