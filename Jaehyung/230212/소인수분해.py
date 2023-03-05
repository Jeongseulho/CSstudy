T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]
    for i in range(len(num)):
        count = 0
        # N을 num으로 나누고 나머지가 존재하면 다음 인덱스로 넘어가야 함
        while N % num[i] == 0: # 25 / 2는 나머지가 존재하기 때문에 실행 X
            N = N / num[i] # 50 / 2 = 25 25를 저장
            count += 1
            result[i] = count # [3, 2, 2, 3, 1]
    result1 = ' '.join(map(str, result))
    print(f'#{tc} {result1}')