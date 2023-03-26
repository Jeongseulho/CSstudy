K = int(input())
num_list = []

for _ in range(K):
    N = int(input())

    if N == 0:
        num_list.pop()
    else:
        num_list.append(N)

print(sum(num_list))
