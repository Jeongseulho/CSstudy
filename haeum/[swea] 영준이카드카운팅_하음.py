T = int(input())

for tc in range(1, T + 1):
    S = input()
    result = []
    card = {'S' : [], 'D' : [], 'H' : [], 'C': []}
    for i in range(0, len(S), 3):
        num = int(S[i + 1]+S[i + 2])
        if num in card[S[i]]:
            result.append("ERROR")
            break
        card[S[i]].append(num)
    else:
        result.append(13 - len(card['S']))
        result.append(13 - len(card['D']))
        result.append(13 - len(card['H']))
        result.append(13 - len(card['C']))

    print(f'#{tc}', *result)