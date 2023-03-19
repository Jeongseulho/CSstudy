N = int(input())

X = N // 5
Y = N % 5
result = []
for i in range(0, X+1):
    if (N - (5 * i)) % 3 == 0:
        K = (N - (5 * i)) // 3
        bag = i + K
        result.append(bag)

if len(result) == 0:
    print(-1)
else:
    print(min(result))