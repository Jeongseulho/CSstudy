def getNums(num):
    ans = []
    while num > 0:
        remain = num % 10
        ans.append(remain)
        num //= 10
    ans.reverse()
    return list(map(int, ans))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = input().split()
    maxVal = -1
    for i in range(N - 1):
        cur = arr[i]
        for j in range(i + 1, N):
            next = arr[j]
            num = int(cur) * int(next)
            nums = getNums(num)
            for k in range(len(nums) - 1):
                curNum = nums[k]
                nextNum = nums[k + 1]
                if curNum > nextNum:
                    break
            else:
                maxVal = max(maxVal, num)

    print(f'#{tc} {maxVal}')
