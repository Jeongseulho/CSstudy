def dfs(start, goal):
    needVisitStack = [start]
    visited = []
    while needVisitStack:
        curNode = needVisitStack.pop()
        if curNode not in visited:
            if goal in adj[curNode]:
                return 1
            visited.append(curNode)
            needVisitStack.extend(adj[curNode])
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
    start, goal = map(int, input().split())
    ans = dfs(start, goal)
    print(f'#{test_case} {ans}')
