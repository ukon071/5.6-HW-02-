def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Проверка на ничью
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return "Ничья"

    return None

def is_valid_move(board, row, col):
    return board[row][col] == " "

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player1 = "X"
    player2 = "O"
    current_player = player1

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")

        try:
            row, col = map(int, input("Введите строку и столбец (1, 2, 3): ").split())
            row -= 1  # Преобразуем в индексы 0-2
            col -= 1  # Преобразуем в индексы 0-2
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Координаты должны быть от 1 до 3. Попробуйте снова.")
                continue
        except ValueError:
            print("Некорректный ввод. Введите два числа через пробел.")
            continue

        if not is_valid_move(board, row, col):
            print("Эта клетка уже занята. Попробуйте снова.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            if winner == "Ничья":
                print("Ничья!")
            else:
                print(f"Игрок {current_player} выиграл!")
            break

        current_player = player2 if current_player == player1 else player1

play_game()