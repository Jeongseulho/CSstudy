def solution(board, moves):
    answer = 0
    basket = []

    for k in moves:
        for i in range(len(board)):
            if board[i][k - 1] != 0:
                basket.append(board[i][k - 1])
                board[i][k - 1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket[-2:] = []
                        answer += 2

                break

    return answer