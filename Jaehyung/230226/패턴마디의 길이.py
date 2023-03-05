T = int(input())
for tc in range(1, T+1):
    data = input()
    for j in range(1, 11):
        lst = []
        for i in range(0, 30, j):
            lst.append(data[i:i+j])
        st = set(lst)
        if 30 % j:
            if len(st) == 2:
                print(f'#{tc} {j}')
                break
        else:
            if len(st) == 1:
                print(f'#{tc} {j}')
                break