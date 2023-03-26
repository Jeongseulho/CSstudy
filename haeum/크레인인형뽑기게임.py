def solution(board, moves):
    basket = []
    answer = 0
    for m in moves:
        for j in range(len(board)):
            if board[j][m - 1]:
                basket.append(board[j][m - 1])
                board[j][m - 1] = 0
                break

        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                answer += 2
                basket.pop()
                basket.pop()
    return answer