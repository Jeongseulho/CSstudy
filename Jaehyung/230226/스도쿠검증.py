# 함수 세개 만들어서 값 확인 후에 맞으면 1 리턴하게 함
# 그 값의 합이 3보다 작으면 0

def width():
    for i in range(9):
        check = set(arr[i])
        if len(check) != 9:
            return 0
    else:
        return 1

def length():
    for j in range(9):
        stack = []
        for i in range(9):
            stack.append(arr[i][j])

        check = set(stack)
        if len(check) != 9:
            return 0
    else:
        return 1

def three():
    # arr[0][0] arr[0][1] arr[0][2]
    # arr[1][0] arr[1][1] arr[1][2]
    # arr[2][0] arr[2][1] arr[2][2]
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            stack = []
            for a in range(3):
                for b in range(3):
                    stack.append(arr[i+a][j+b])
            check = set(stack)
            if len(check) != 9:
                return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    subnum = width() + length() + three()

    if subnum != 3:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')