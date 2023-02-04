# import sys
# sys.stdin = open("input.txt", "r")
def getMax(cnts):
    maxValue = cnts[0]
    for i in range(1, len(cnts)):
        if maxValue < cnts[i]:
            maxValue = cnts[i]
    return maxValue


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0 for _ in range(10001)]
    for _ in range(N):
        type, A, B = map(int, input().split())

        if type == 1:
            for i in range(A, B+1):
                cnts[i] += 1

        if type == 2:
            for i in range(A, B+1, 2):
                cnts[i] += 1

        if type == 3:
            if A % 2 == 0:
                for i in range(A, B+1):
                    if i % 4 == 0:
                        cnts[i] += 1
            else:
                for i in range(A, B+1):
                    if i % 3 == 0 and i % 10 != 0:
                        cnts[i] += 1

    print(f'#{test_case} {getMax(cnts)}')
