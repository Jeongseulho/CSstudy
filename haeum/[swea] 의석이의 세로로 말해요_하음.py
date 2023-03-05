T = int(input())

for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    result = ''
    mx = max(len(arr[i]) for i in range(5))

    for i in range(mx):
        for j in range(5):
            try:
                result += arr[j][i]
            except IndexError:
                pass

    print(f'#{tc} {result}')