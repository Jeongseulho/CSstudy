import sys
sys.stdin = open("s_input.txt", "r")

T = int(input()) # 테스트 케이스
for t in range(1, T+1):
    numbers = [0] * 5001 # 정류장 번호 (0번은 버림)
    N = int(input()) # 버스 대 수
    buses = []
    # N 이후로 엔터 기준으로 입력될 N 개의 버스의 노선을 저장할 리스트
    for n in range(N):
        bus = tuple(map(int, input().split()))
        # '1 3'이 입력되면 (1,3)으로 저장됨
        buses.append(bus)
    P = int(input()) # 확인해야 할 정류장 개수
    stops = []
    for p in range(P):
        stop = int(input())
        stops.append(stop)

# print(f'T:{T}, N:{N}, 버스노선:{buses}, P:{P}, 정류장:{stops}')
### 여기까지가 값들을 받는 부분
    for i in range(N):
    # buses[i][0]부터 buses[i][1]까지의 범위를 가진 리스트 만듦 (노선 i)
    # 노선 = [1, 2, 3, 4]
    # numbers[노선[i]] += 1
        busstop = [i for i in range(buses[i][0], buses[i][1]+1)]
        for j in busstop:
            numbers[j] += 1
        # print(numbers[:30])

    rst = []
    for k in stops:
        rst.append(numbers[k])

    result = ' '.join(map(str, rst))
    print(f'#{t} {result}')

