def solution(cardArr):
    if len(set(cardArr)) != len(cardArr):
        return "ERROR"
    Scount = Dcount = Hcount = Ccount = 13
    for i in range(len(cardArr)):
        if cardArr[i][0] == 'S':
            Scount -= 1
        elif cardArr[i][0] == 'D':
            Dcount -= 1
        elif cardArr[i][0] == 'H':
            Hcount -= 1
        elif cardArr[i][0] == 'C':
            Ccount -= 1

    return Scount, Dcount, Hcount, Ccount


T = int(input())
for tc in range(1, T + 1):
    inputStr = input()
    N = len(inputStr)
    cardArr = []
    for i in range(0, N, 3):
        card = inputStr[i:i + 3]
        cardArr.append(card)

    result = solution(cardArr)
    if result == "ERROR":
        print(f'#{tc} {result}')
    else:
        print(f'#{tc}', *result)
