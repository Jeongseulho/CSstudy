N = int(input())
ans = []
for i in range(1, N + 1):
    strNum = str(i)
    clapCnt = strNum.count('3') + strNum.count('6') + strNum.count('9')
    if clapCnt:
        ans.append('-' * clapCnt)
    else:
        ans.append(i)

print(*ans)
