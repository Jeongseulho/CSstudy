T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cardDec = input().split()
    mid = N // 2

    if N % 2:
        firstDec = cardDec[:mid + 1]
        secondDec = cardDec[mid + 1:]
        ans = []
        for i in range(mid):
            ans.append(firstDec[i])
            ans.append(secondDec[i])
        ans.append(firstDec[mid])
    else:
        firstDec = cardDec[:mid]
        secondDec = cardDec[mid:]
        ans = []
        for i in range(mid):
            ans.append(firstDec[i])
            ans.append(secondDec[i])

    print(f'#{tc}', *ans)
