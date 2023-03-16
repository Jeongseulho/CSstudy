N = int(input())
arr = []
for _ in range(N):
    W, H = map(int, input().split())
    if not arr:
        arr.append([W, H, 1])
        continue
    cnt = 1
    for i in range(len(arr)):
        if arr[i][0] < W and arr[i][1] < H:
            arr[i][2] += 1
        elif arr[i][0] > W and arr[i][1] > H:
            cnt += 1
    arr.append([W, H, cnt])
for i in range(N - 1):
    print(arr[i][2], end=' ')
print(arr[N - 1][2])