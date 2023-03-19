N = int(input())
data = [list(map(int, input().split())) + [1] for _ in range(N)]

for cur in data:
    for nex in data:
        if cur[0] < nex[0] and cur[1] < nex[1]:
            cur[2] += 1
    print(cur[2], end=' ')