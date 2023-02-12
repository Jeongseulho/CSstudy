import sys
sys.stdin = open("ladder_input.txt", "r")

def side(ladder, r, c):  # 옆으로 가기
    if c - 1 > -1 and ladder[r][c - 1] == 1: #될 때까지 옆으로 가쇼
        c -= 1
        while c - 1 > -1 and ladder[r + 1][c] == 0:
            c -= 1
    elif c + 1 < 100 and ladder[r][c + 1] == 1:
        c += 1
        while c + 1 < 100 and ladder[r + 1][c] == 0:
            c += 1
    return c


for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[0][i] == 1:  # 사다리 시작점을 만남!
            r, c = 1, i
            while r < 99:
                c = side(ladder, r, c)
                r += 1
            if ladder[r][c] == 2:
                result = i
                break

    print(f'#{tc} {result}')
