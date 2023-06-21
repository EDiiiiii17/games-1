import random

board = []
for _ in range(10):
    row = [' ' for _ in range(10)]
    board.append(row)

player_row = 5
player_col = 5
board[player_row][player_col] = '@'

level = 1
num_enemies = level
moves = 5
total_moves = 0

for _ in range(num_enemies):
    enemy_row = random.randint(0, 9)
    enemy_col = random.randint(0, 9)

    while (enemy_row == player_row and enemy_col == player_col) or board[enemy_row][enemy_col] == '+':
        enemy_row = random.randint(0, 9)
        enemy_col = random.randint(0, 9)

    board[enemy_row][enemy_col] = '+'

while num_enemies > 0 and moves > 0:
    print(' *' * 11)

    for row in board:
        print('*', end=' ')
        for cell in row:
            print(cell, end=' ')
        print('*')

    print(' *' * 11)

    direction = input("Введите направление (вверх - w, вниз - s, влево - a, вправо - d): ")

    board[player_row][player_col] = ' '

    if direction == 'w' and player_row > 0:
        player_row -= 1
    elif direction == 's' and player_row < 9:
        player_row += 1
    elif direction == 'a' and player_col > 0:
        player_col -= 1
    elif direction == 'd' and player_col < 9:
        player_col += 1

    if board[player_row][player_col] == '+':

        board[player_row][player_col] = ' '
        num_enemies -= 1
        moves += 5

    if num_enemies == 0:
        level += 1
        num_enemies = level
        moves += 1

        for _ in range(num_enemies):
            enemy_row = random.randint(0, 9)
            enemy_col = random.randint(0, 9)

            while (enemy_row == player_row and enemy_col == player_col) or board[enemy_row][enemy_col] == '+':
                enemy_row = random.randint(0, 9)
                enemy_col = random.randint(0, 9)

            board[enemy_row][enemy_col] = '+'

    board[player_row][player_col] = '@'
    moves -= 1
    total_moves += 1

    print("Осталось ходов:", moves)

if num_enemies == 0:
    print("Поздравляю! Вы съели всех врагов!")
else:
    print("У вас закончились ходы. Игра окончена!")
print("Количество сделанных ходов:", total_moves)

