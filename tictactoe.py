def print_board(board):
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")

board = [[' ' for _ in range(3)] for _ in range(3)]
print_board(board)

