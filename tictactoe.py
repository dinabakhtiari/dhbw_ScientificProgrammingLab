import math

def print_board(board):
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")

def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] and b[i][0] != ' ': return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] and b[0][i] != ' ': return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != ' ': return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != ' ': return b[0][2]
    if all(cell != ' ' for row in b for cell in row): return 'Tie'
    return None

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

def get_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome! You are 'X' and AI is 'O'.")
    
    while True:
        print_board(board)
        try:
            user_input = input("\nEnter row and col (0-2) e.g '0 1': ").split()
            r, c = int(user_input[0]), int(user_input[1])
            
            if board[r][c] != ' ':
                print("Invalid move! Cell already taken.")
                continue
        except (ValueError, IndexError):
            print("Please enter two numbers between 0 and 2.")
            continue

        board[r][c] = 'X'
        if check_winner(board): break
        
        print("\nAI is thinking...")
        ai_move = get_best_move(board)
        if ai_move != (-1, -1):
            board[ai_move[0]][ai_move[1]] = 'O'
        
        if check_winner(board): break

    print_board(board)
    result = check_winner(board)
    if result == 'Tie':
        print("\nIt's a Tie! 🤝")
    else:
        print(f"\nGame Over! Winner is: {result} 🎉")

if __name__ == "__main__":
    play_game()