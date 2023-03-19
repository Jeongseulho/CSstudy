N = int(input())
# 666이 들어간 모든 수 체크하면 된다..
# N이 666이 들어간 숫자 중 몇번 째 인지 밝혀내는 것이기 때문에
# 1번 째인 666부터 1씩 늘어나게 해서
# 666이 들어간 숫자면 N에서 1씩 빼서 0이 되면 해당 숫자를 출력하게 하면 된다..
first = 666
while True:
    if '666' in str(first):
        N -= 1
        if N == 0:
            print(first)
            break
    first += 1