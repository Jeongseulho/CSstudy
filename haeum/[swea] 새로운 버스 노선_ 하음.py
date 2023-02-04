T = int(input())

for tc in range(1, T + 1):
    allBusStop = [0] * 1001
    N = int(input())
    maxV = allBusStop[0]

    for _ in range(N):
        busType, A, B = map(int,input().split())
        allBusStop[A] += 1
        allBusStop[B] += 1

        if busType == 1: # 일반
            for i in range(A + 1, B):
                allBusStop[i] += 1

        elif busType == 2: # 급행
            for i in range(A + 2, B, 2):
                allBusStop[i] += 1

        elif busType == 3: # 광역 급행
            if A % 2: # 홀수
                for k in range(A + 1, B):
                    if (not (k % 3)) and (k % 10):
                        allBusStop[k] += 1
            else:
                for k in range(A + 1, B):
                    if not(k % 4):
                        allBusStop[k] += 1

    for i in allBusStop:
        if i > maxV:
            maxV = i

    print(f'#{tc} {maxV}')