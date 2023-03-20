def hanoi(n, start, mid, end):
    if n == 1:  # 원판이 1개인 상황이면 그냥 옮김
        moves.append([start, end])
    else:  # 원판이 2개 이상이면 3단게로 옮겨야함
        # 1단계 : 맨 아래 있는 제일 큰 원판 제외 나머지를 start에서 mid로 옮김
        hanoi(n - 1, start, end, mid)
        moves.append([start, end])  # 2단계 : 맨 아래 있는 제일 큰 원판을 start에서 end로 옮김
        hanoi(n - 1, mid, start, end)  # 3단계 : mid에 있던 나머지 원판을 end로 옮김


N = int(input())
moves = []
hanoi(N, 1, 2, 3)  # N개의 원판을 start=1로부터 end=3으로 옮기기

print(len(moves))
for move in moves:
    print(*move)
