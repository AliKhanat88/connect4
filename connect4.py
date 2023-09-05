import random
import math


def check_move(board, turn, col, pop):
    rows = len(board) // 7
    if col > 6 or col < 0:
        return False
    if pop == True:
        is_empty = True
        for i in range(rows):
            if board[i * 7 + col] != 0:
                is_empty = False
                break
        if is_empty == True:
            return False
        if turn != board[col]:
            return False 
    if pop == False:
        is_filled = True
        for i in range(rows):
            if board[i * 7 + col] == 0:
                is_filled = False
                break
        if is_filled == True:
            return False
    return True

def apply_move(board, turn, col, pop):
    rows = len(board) // 7
    if pop == True:
        for i in range(rows-1):
            board[i * 7 + col] = board[(i+1) * 7 + col]
        board[(rows-1) * 7 + col] = 0
    else:
        for i in range(rows):
            if board[i * 7 + col] == 0:
                board[i * 7 + col] = turn
                break
    return board.copy()

def check_victory(board, who_played):
    count_1 = 0
    count_2 = 0
    is_connect_1 = False
    is_connect_2 = False
    rows = len(board) // 7
    # Row Check
    for i in range(rows):
        for j in range(7):
            if board[i * 7 + j] == 1:
                count_1 += 1
                count_2 = 0
            elif board[i * 7 + j] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1 = 0
                count_2 = 0
            if count_1 >= 4:
                is_connect_1 = True
            if count_2 >= 4:
                is_connect_2 = True
        count_1 = 0
        count_2 = 0
    count_1 = 0
    count_2 = 0
    # Column Check
    for col in range(7):
        for row in range(rows):
            if board[row * 7 + col] == 1:
                count_1 += 1
                count_2 = 0
            elif board[row * 7 + col] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1 = 0
                count_2 = 0
            if count_1 >= 4:
                is_connect_1 = True
            if count_2 >= 4:
                is_connect_2 = True
        count_1 = 0
        count_2 = 0
    # Diagnol 1
    for row in range(rows):
        col = 0
        for j in range(row, -1, -1):
            if col > 6:
                break
            if board[j * 7 + col] == 1:
                count_1 += 1
                count_2 = 0
            elif board[j * 7 + col] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1 = 0
                count_2 = 0
            if count_1 >= 4:
                is_connect_1 = True
            if count_2 >= 4:
                is_connect_2 = True
            col += 1
        count_1 = 0
        count_2 = 0 
    for col in range(7):
        row = rows - 1
        for j in range(row, -1, -1):
            if col > 6:
                break
            if board[j * 7 + col] == 1:
                count_1 += 1
                count_2 = 0
            elif board[j * 7 + col] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1 = 0
                count_2 = 0
            if count_1 >= 4:
                is_connect_1 = True
            if count_2 >= 4:
                is_connect_2 = True
            col += 1
        count_1 = 0
        count_2 = 0
    # Diagnol 2
    for row in range(rows):
        col = 0
        for j in range(row, rows, 1):
            if col > 6:
                break
            if board[j * 7 + col] == 1:
                count_1 += 1
                count_2 = 0
            elif board[j * 7 + col] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1 = 0
                count_2 = 0
            if count_1 >= 4:
                is_connect_1 = True
            if count_2 >= 4:
                is_connect_2 = True
            col += 1
        count_1 = 0
        count_2 = 0 
    for col in range(7):
        row = 0
        for j in range(row, rows, 1):
            if col > 6:
                break
            if board[j * 7 + col] == 1:
                count_1 += 1
                count_2 = 0
            elif board[j * 7 + col] == 2:
                count_2 += 1
                count_1 = 0
            else:
                count_1 = 0
                count_2 = 0
            if count_1 >= 4:
                is_connect_1 = True
            if count_2 >= 4:
                is_connect_2 = True
            col += 1
        count_1 = 0
        count_2 = 0
    
    if is_connect_1 == True and is_connect_2 == True:
        if who_played == 1:
            return 2
        else:
            return 1
    elif is_connect_1 == True:
        return 1
    elif is_connect_2 == True:
        return 2
    else:
        return 0

def computer_move(board, turn, level):
    # implement your function here

    if level == 1:
        while True:
            col = random.randint(0, 6)
            is_pop = random.randint(0, 1)
            if check_move(board, turn, col, is_pop == 1):
                return (col, is_pop == 1)
    elif level == 2:
        rows = len(board) // 7
        for j in range(7):
            if check_move(board, turn, j, False):
                temp = board.copy()
                apply_move(temp, turn, j, False)
                if check_victory(temp, turn) == turn:
                    return j, False
        for j in range(7):
            if check_move(board, 1, j, True):
                temp = board.copy()
                if check_victory(temp, turn) == turn:
                    return j, True
        for j in range(7):
            if turn == 2: 
                if check_move(board, 1, j, False):
                    temp = board.copy()
                    apply_move(temp, 1, j, False)
                    if check_victory(temp, 1) == 1:
                        return j, False
            if turn == 1:
                if check_move(board, 2, j, False):
                    temp = board.copy()
                    apply_move(temp, 2, j, False)
                    if check_victory(temp, 2) == 2:
                        return j, False
        while True:
            col = random.randint(0, 6)
            is_pop = random.randint(0, 1)
            if check_move(board, turn, col, is_pop == 1):
                return (col, is_pop == 1)
def display_board(board):
    rows = len(board) // 7
    print("----------------Board-----------------------")
    print("0 1 2 3 4 5 6")
    print("-------------")
    for i in range(rows-1, -1, -1):
        for j in range(7):
            print(board[i * 7 + j], end = " ")
        print()

def menu():
    board = [0,0,0,0,0,0,0,  0,0,0,0,0,0,0,  0,0,0,0,0,0,0,  0,0,0,0,0,0,0,  0,0,0,0,0,0,0,  0,0,0,0,0,0,0]
    turn = 1
    play_against_computer = int(input("Press 0 for playing against human and 1 for playing againt AI: "))
    if play_against_computer == 1:
        print("What should be the dIfficulty level for AI?")
        level = int(input("Press 1 for level 1 and 2 for level 2 : "))
    while True:
        if play_against_computer == 1:
            if turn == 2:
                col , pop = computer_move(board, turn, level)
            else:
                display_board(board)
                print(f"Turn for player {turn}")
                col = int(input("Enter column in which you want to insert: "))
                pop = int(input("Want to pop out? 0 for No and anything else for Yes: "))
            if pop == 0:
                pop = False
            else:
                pop = True
            if check_move(board, turn, col, pop):
                apply_move(board, turn, col, pop)
                if check_victory(board, turn) == 0:
                    if turn == 1:
                        turn = 2
                    else:
                        turn = 1
                    continue
                else:
                    winner = check_victory(board, turn)
                    print(f"CheckMate! the winner is {winner}")
                    display_board(board)
                    return
            else:
                print("Invalid Move!")
                continue
        else:
            display_board(board)
            print(f"Turn for player {turn}")
            col = int(input("Enter column in which you want to insert:- "))
            pop = int(input("Want to pop out? 0 for No and 1 for Yes: "))
            if pop == 0:
                pop = False
            else:
                pop = True
            if check_move(board, turn, col, pop):
                apply_move(board, turn, col, pop)
                if check_victory(board, turn) == 0:
                    if turn == 1:
                        turn = 2
                    else:
                        turn = 1
                    continue
                else:
                    winner = check_victory(board, turn)
                    print(f"CheckMate! the winner is {winner}")
                    return
            else:
                print("Invalid Move!")
                continue
        

if __name__ == "__main__":
    menu()




    
