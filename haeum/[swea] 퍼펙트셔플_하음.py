T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    mid = N // 2
    if N % 2:
        mid += 1
    result = []
    for i in range(mid):
        result.append(card[i])
        try:
            result.append(card[mid + i])
        except IndexError:
            pass
    print(f'#{tc}', *result)