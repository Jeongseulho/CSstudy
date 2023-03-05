import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 진행으로 필요한 방향은
    # 하 좌 우
    d1 = [1, 0, 0]
    d2 = [0, -1, -1]
    r, c = 0,0
    dir = 0
    for i in range(100):
        if arr[r][c+i] == 1:
        # 첫줄에서 시작점을 찾기
            while r < 100:
                if arr[r][c-1] == 1:
                    dir = 1
                if arr[r][c+1] == 1:
                    dir = 2


    print(f'{tc} {result}')
