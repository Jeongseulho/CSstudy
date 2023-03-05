def checkAns(arr):
    if arr[0] != arr[1]:
        return False
    return True


T = int(input())
for tc in range(1, T + 1):
    inputStr = input()

    ans = 0
    for k in range(1, 11):
        arr = []
        for i in range(0, 30, k):
            arr.append(inputStr[i:i + k])
        if checkAns(arr):
            ans = k
            break

    print(f'#{tc} {k}')
