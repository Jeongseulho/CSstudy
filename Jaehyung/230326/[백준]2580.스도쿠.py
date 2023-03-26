data = [list(input().split()) for _ in range(9)]

emp = []
for i in range(9):
    for j in range(9):
        if data[i][j] == '0':
            emp.append((i,j))