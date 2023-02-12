T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    N_arr = [2, 3, 5, 7, 11]
    arr = [0] * 5
    cnt = i = 0

    while N > 1 and i < 5: # 뒷 부분은 쿠션...
        if N % N_arr[i] == 0:
            cnt += 1
            N //= N_arr[i]
            arr[i] = cnt
        else:
            cnt = 0
            i += 1

    print(f'#{tc}', *arr)