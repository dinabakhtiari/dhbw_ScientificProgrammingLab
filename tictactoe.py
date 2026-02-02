def print_board(board):
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")

board = [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] and b[i][0] != ' ': return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] and b[0][i] != ' ': return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != ' ': return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != ' ': return b[0][2]
    
    if all(cell != ' ' for row in b for cell in row): return 'Tie'
    return None

print_board(board)
import math

def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == 'O': return 10 - depth 
    if result == 'X': return depth - 10  
    if result == 'Tie': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
    
test_board = [
    ['O', 'O', ' '],
    ['X', 'X', ' '],
    [' ', ' ', ' ']
]
score = minimax(test_board, 0, True)
print(f"Max Score possible for this board: {score}")