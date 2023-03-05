T = int(input())
for tc in range(1, T + 1):
    bits = list(input())
    N = len(bits)
    myBits = ['0'] * N
    cnt = 0
    idx = 0
    while True:
        if myBits == bits:
            break
        if myBits[idx] != bits[idx]:
            myBits[idx:] = bits[idx] * len(myBits[idx:])
            cnt += 1
        idx += 1
    print(f'#{tc} {cnt}')
