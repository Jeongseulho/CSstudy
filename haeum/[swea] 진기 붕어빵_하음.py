T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))

    arrive.sort()
    make = [0]

    for i in range(1, arrive[-1] + 1):
        if not i % M:
            make.append(K)
        else:
            make.append(0)

    result = 'Possible'
    for people in arrive:
        for i in range(1, people + 1):
            if make[i]:
                make[i] -= 1
                break
        else:
            result = 'Impossible'


    print(f'#{tc} {result}')