T = int(input())
num_lst = ['3', '6', '9']
rst = []
for i in range(1, T+1):
    k = str(i)
    if '3' in k or '6' in k or '9' in k:
        sub = ''
        for j in k:
            if j not in num_lst:
                continue
            else:
                sub += '-'
        rst.append(sub)
    else:
        rst.append(k)

print(*rst)