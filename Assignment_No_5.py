def print_board(board, N):
    for row in range(N):
        line = ""
        for col in range(N):
            if board[row][col] == 1:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queen(board, col, N):
    if col >= N:
        print_board(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queen(board, col + 1, N) or res
            board[i][col] = 0 
    return res

def n_queen(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queen(board, 0, N):
        print(f"No solution exists for {N} queens.")

n = int(input("Enter size of board : "))
n_queen(n)