for tc in range(1,11):
    input()
    pattern = input()
    str1 = input()
    cnt = 0

    for k in range(len(str1)):
        j = 0
        while j < len(pattern):
            if pattern[j] == str1[k]:
                k += 1
                j += 1
                if j == len(pattern):
                    cnt += 1
                    break
            else:
                break

    print(f'#{tc} {cnt}')
