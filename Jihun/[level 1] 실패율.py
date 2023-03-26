result = []
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
dict = {}


def solution(N, stages):
    for i in range(1, N+1):
        result = 0
        arrival = []
        not_clear = []
        for j in stages:
            if i <= j:
                arrival.append(j)
            if i == j:
                not_clear.append(j)

        result = (len(not_clear) / len(arrival))
        dict[i] = result
        sorted(dict.keys(), reverse=True)

    return print(sorted(dict.keys(), reverse=True))


solution(N, stages)
