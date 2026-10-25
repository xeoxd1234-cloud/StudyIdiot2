"""Tic-Tac-Toe — Minimax with Alpha-Beta Pruning."""

import math

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def winner(board):
    for i, j, k in WIN_LINES:
        if board[i] and board[i] == board[j] == board[k]:
            return board[i]
    return "Draw" if all(board) else None


def minimax(board, turn, alpha=-math.inf, beta=math.inf):
    result = winner(board)
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    scores = []
    for index in range(9):
        if not board[index]:
            board[index] = turn
            next_turn = "O" if turn == "X" else "X"
            scores.append(minimax(board, next_turn, alpha, beta))
            board[index] = ""

            if turn == "O":
                alpha = max(alpha, max(scores))
            else:
                beta = min(beta, min(scores))
            if alpha >= beta:
                break

    return max(scores) if turn == "O" else min(scores)


if __name__ == "__main__":
    initial_board = ["O", "X", "X", "O", "X", "", "", "", ""]
    print("Minimax score:", minimax(initial_board, "O"))
