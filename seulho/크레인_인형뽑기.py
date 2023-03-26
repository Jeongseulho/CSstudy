def solution(board, moves):
    N = len(board)
    answer = 0
    basket_stack = []
    for moveJ in moves:
        for i in range(N):
            doll = board[i][moveJ - 1]

            if doll:
                board[i][moveJ - 1] = 0
                basket_stack.append(doll)
                cnt = countDelDoll(basket_stack)
                answer += cnt
                break

    return answer


def countDelDoll(basket_stack):
    cnt = 0
    while True:
        if len(basket_stack) < 2 or basket_stack[-1] != basket_stack[-2]:
            return cnt
        basket_stack.pop()
        basket_stack.pop()
        cnt += 2
