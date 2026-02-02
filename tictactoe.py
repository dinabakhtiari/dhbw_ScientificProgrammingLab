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
board[0][0] = 'X'
board[0][1] = 'X'
board[0][2] = 'X'
print_board(board)

winner = check_winner(board)
print(f"Result {winner}")