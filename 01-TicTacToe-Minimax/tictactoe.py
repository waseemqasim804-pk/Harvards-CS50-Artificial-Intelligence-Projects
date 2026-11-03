"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {
        (i, j)
        for i in range(3)
        for j in range(3)
        if board[i][j] == EMPTY
    }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise ValueError("Invalid action: action cannot be None.")

    try:
        i, j = action
    except (TypeError, ValueError):
        raise ValueError(f"Invalid action: {action} is not a valid (row, col) action.")

    if not (0 <= i <= 2 and 0 <= j <= 2):
        raise IndexError(f"Invalid action: coordinates ({i}, {j}) out of bounds.")

    if board[i][j] != EMPTY:
        raise ValueError(f"Invalid action: cell ({i}, {j}) is already occupied.")

    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] is not EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] is not EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]

    # Check main diagonal
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Check anti-diagonal
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_val = -math.inf
        best_action = None
        alpha = -math.inf
        beta = math.inf

        for action in actions(board):
            val = _min_value(result(board, action), alpha, beta)
            if val > best_val:
                best_val = val
                best_action = action
            alpha = max(alpha, best_val)
            if best_val == 1:
                return best_action

        return best_action

    else:
        best_val = math.inf
        best_action = None
        alpha = -math.inf
        beta = math.inf

        for action in actions(board):
            val = _max_value(result(board, action), alpha, beta)
            if val < best_val:
                best_val = val
                best_action = action
            beta = min(beta, best_val)
            if best_val == -1:
                return best_action

        return best_action


def _max_value(board, alpha, beta):
    """
    Helper function to compute maximum achievable utility for player X.
    """
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, _min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v


def _min_value(board, alpha, beta):
    """
    Helper function to compute minimum achievable utility for player O.
    """
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, _max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v
