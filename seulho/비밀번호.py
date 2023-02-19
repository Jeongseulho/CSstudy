T = 10
for test_case in range(1, T + 1):
    N, nums = input().split()
    stack = []
    for num in nums:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    print(f'#{test_case} ', ''.join(stack))
