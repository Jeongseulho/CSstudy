mat = [list(map(int, input().split()))for _ in range(9)]
vst1 = [[False]*9 for _ in range(9)]
vst2 = [[False]*9 for _ in range(9)]
vst3 = [[False]*9 for _ in range(9)]


def box(i, k):
    return i//3*3+j//3


for i in range(9):
    for j in range(9):
        if mat[i][j]:
            vst1[i][mat[i][j]-1] = True
            vst2[i][mat[i][j]-1] = True
            vst3[box(i, j)][mat[i][j]-1] = True


def back(i, j):
    if i == 9:
        for x in mat:
            print(*x)
        return

    if mat[i][j]:
        back(i(j+1)//9, (j+1) % 9)
        return

        for k in range(9):
            if vst[i][k] or vst2[j][k] or vst3[box(i, j)][k]:
                continue
