N = int(input())

i = N // 5
while True:
    if not N % 5:
        result = N // 5
        break
    elif not (N % 5) % 3:
        result = (N // 5)
        result += (N % 5) // 3
        break
    elif not (N - (5 * i)) % 3:
        result = i
        result += (N - (5 * i)) // 3
        break

    if i == 0:
        if not N % 3:
            result = (N // 3)
            break
        result = -1
        break
    i -= 1

print(result)