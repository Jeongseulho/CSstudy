function solution(board, moves) {
  N = board.length;
  let answer = 0;
  const basketStack = [];
  for (let moveJ of moves) {
    for (let i = 0; i < N; i++) {
      const doll = board[i][moveJ - 1];
      if (doll) {
        board[i][moveJ - 1] = 0;
        basketStack.push(doll);
        answer += countDelDoll(basketStack);
        break;
      }
    }
  }
  return answer;
}

function countDelDoll(basketStack) {
  let cnt = 0;
  while (true) {
    if (
      basketStack.length < 2 ||
      basketStack[basketStack.length - 1] != basketStack[basketStack.length - 2]
    ) {
      return cnt;
    }
    basketStack.pop();
    basketStack.pop();
    cnt += 2;
  }
}

const board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];

const moves = [1, 5, 3, 5, 1, 2, 1, 4];

console.log(solution(board, moves));
