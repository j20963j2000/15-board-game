import numpy as np
import copy
from random import choice

print("   ")
# decide if User first 
user_first = input("User First ? (y/n)").lower()

while True:
    legal_input = ["y", "n"]
    if user_first in legal_input:
        break
    else:
        user_first = input("User First ? (please type y or n)").lower()

# deside the size of the game board

board_size = input("Board Size ? (4/6)")
print("  ")
while True:
    legal_input = [4, 6]
    if int(board_size) in legal_input:
        break
    else:
        board_size = input("Board Size ? (please type 4 or 6)")

board_size = int(board_size)

board = [[0 for i in range(board_size)] for i in range(board_size)]

# print('\n'.join(' '.join(str(cell) for cell in row) for row in board)) 

for i in board:
    if board_size == 4:
        print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
    else:
        print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
print("   ")

if board_size == 4: 
    total_chess = [2, 3, 5, 8, 13]
    User_chess = [2, 3, 5, 8, 13]
    AI_chess = [2, 3, 5, 8, 13]
else:
    total_chess = [2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13]
    User_chess = [2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13]
    AI_chess = [2, 2, 3, 3, 5, 5, 8, 8, 8, 13, 13]

playing_game = True

def user_play_first(playing_game, board, User_chess, AI_chess):
    user_board = copy.deepcopy(board)
    ai_board = copy.deepcopy(board)

    while playing_game:
        print("----------Starting Next round----------")
        print("  ")
        print("User_chess :", User_chess)
        print("AI_chess :", AI_chess) 
        print("  ")
        u_row, u_col, u_weight = input("input(row, col, weight)").split()
        u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
        # check input if is legal
        while True:
            if (u_row <= board_size) and (u_col <= board_size):
                if board[u_row][u_col] == 0:
                    break
                else:
                    print("Had A Value Already !")
                    u_row, u_col, u_weight = input("input(row, col, weight)").split()
                    u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
            else:
                print("Out of Board Range !")
                u_row, u_col, u_weight = input("input(row, col, weight)").split()
                u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
        
        while True:
            if u_weight in User_chess:
                break
            else:
                print("You need to choose another card !")
                u_row, u_col, u_weight = input("input(row, col, weight)").split()
                u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)

        print("=" * 20)
        print("User :", u_row, u_col, u_weight)
        print("=" * 20)
        # card_total_numbers = set([2, 3, 5, 8, 13])
        # if u_weight not in card_total_numbers:
        #     print("didnt find this card !")

        card_idx = User_chess.index(u_weight)
        User_chess.pop(card_idx)
        board[u_row][u_col] = u_weight           # record on board
        user_board[u_row][u_col] = u_weight      # record on user board for calculating user score

        '''
        check and mark
        '''
        board = check_and_mark(board)

        # print('\n'.join(' '.join(str(cell) for cell in row) for row in board))  # show the board on the screen
        for i in board:
            if board_size == 4:
                print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
            else:
                print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        print("User_chess :", User_chess)
        print("AI_chess :", AI_chess)  

        # AI's turn
        ai_row, ai_col, ai_weight = AI_move(board, ai_board, user_board, AI_chess)
        print("=" * 20)
        print("AI :", ai_row, ai_col, ai_weight)
        print("=" * 20)


        card_idx = AI_chess.index(ai_weight)
        AI_chess.pop(card_idx)
        board[ai_row][ai_col] = ai_weight
        ai_board[ai_row][ai_col] = ai_weight      # record on AI board for calculating ai score

        '''
        check and mark
        '''
        board = check_and_mark(board)

        # print('\n'.join(' '.join(str(cell) for cell in row) for row in board))  # show the board on the screen
        for i in board:
            if board_size == 4:
                print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
            else:
                print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        print("User_chess :", User_chess)
        print("AI_chess :", AI_chess)  
        print(" "*20)

        if User_chess == [] and AI_chess == []:
            print("*****End of game*****")
            print("User remaining card value :")
            user_score = compute_score(board, user_board)
            # print('\n'.join(' '.join(str(cell) for cell in row) for row in user_board))
            for i in user_board:
                if board_size == 4:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
                else:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
            # print(user_score)
            print("AI remaining card value :")
            ai_score = compute_score(board, ai_board)
            # print('\n'.join(' '.join(str(cell) for cell in row) for row in ai_board))
            for i in ai_board:
                if board_size == 4:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
                else:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
            # print(ai_score)
            print("Score | User :{user} | AI :{ai}".format(user = user_score, ai = ai_score))
            if user_score > ai_score:
                print("user win !")
            elif ai_score > user_score:
                print("ai win !")
            else:
                user_remaining = []
                for id_row, row in enumerate(user_board):
                    for id_col, col in enumerate(row):
                        if user_board[id_row][id_col] in total_chess:
                            user_remaining.append(user_board[id_row][id_col])

                ai_remaining = []
                for id_row, row in enumerate(ai_board):
                    for id_col, col in enumerate(row):
                        if ai_board[id_row][id_col] in total_chess:
                            ai_remaining.append(ai_board[id_row][id_col])

                user_max = max(user_remaining)
                ai_max = max(ai_remaining)
                if user_max > ai_max:
                    print("user win !")
                elif ai_max > user_max:
                    print("ai win !")
                else:
                    print("tie game !")
            playing_game = False 

def ai_play_first(playing_game, board, User_chess, AI_chess):
    user_board = copy.deepcopy(board)
    ai_board = copy.deepcopy(board)

    while playing_game:
        print("----------Starting Next round----------")
        print("  ")
        print("User_chess :", User_chess)
        print("AI_chess :", AI_chess) 
        print("  ")

        # AI's turn
        ai_row, ai_col, ai_weight = AI_move(board, ai_board, user_board, AI_chess)
        print("=" * 20)
        print("AI :", ai_row, ai_col, ai_weight)
        print("=" * 20)

        card_idx = AI_chess.index(ai_weight)
        AI_chess.pop(card_idx)
        board[ai_row][ai_col] = ai_weight
        ai_board[ai_row][ai_col] = ai_weight      # record on AI board for calculating ai score

        '''
        check and mark
        '''
        board = check_and_mark(board)

        # print('\n'.join(' '.join(str(cell) for cell in row) for row in board))  # show the board on the screen
        for i in board:
                if board_size == 4:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
                else:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        print("User_chess :", User_chess)
        print("AI_chess :", AI_chess)  
        print(" "*20)

        u_row, u_col, u_weight = input("input(row, col, weight)").split()
        u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
        # check input if is legal
        while True:
            if (u_row <= board_size) and (u_col <= board_size):
                if board[u_row][u_col] == 0:
                    break
                else:
                    print("Had A Value Already !")
                    u_row, u_col, u_weight = input("input(row, col, weight)").split()
                    u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
            else:
                print("Out of Board Range !")
                u_row, u_col, u_weight = input("input(row, col, weight)").split()
                u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
        
        while True:
            if u_weight in User_chess:
                break
            else:
                print("You need to choose another card !")
                u_row, u_col, u_weight = input("input(row, col, weight)").split()
                u_row, u_col, u_weight = int(u_row), int(u_col), int(u_weight)
        print("=" * 20)
        print("User :", u_row, u_col, u_weight)
        print("=" * 20)

        card_idx = User_chess.index(u_weight)
        User_chess.pop(card_idx)
        board[u_row][u_col] = u_weight           # record on board
        user_board[u_row][u_col] = u_weight      # record on user board for calculating user score

        '''
        check and mark
        '''
        board = check_and_mark(board)

        # print('\n'.join(' '.join(str(cell) for cell in row) for row in board))  # show the board on the screen
        for i in board:
                if board_size == 4:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
                else:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        print("User_chess :", User_chess)
        print("AI_chess :", AI_chess)  

        if User_chess == [] and AI_chess == []:
            print("*****End of game*****")
            print("User remaining card value :")
            user_score = compute_score(board, user_board)
            # print('\n'.join(' '.join(str(cell) for cell in row) for row in user_board))
            for i in user_board:
                if board_size == 4:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
                else:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
            # print(user_score)
            print("AI remaining card value :")
            ai_score = compute_score(board, ai_board)
            # print('\n'.join(' '.join(str(cell) for cell in row) for row in ai_board))
            for i in ai_board:
                if board_size == 4:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2}".format(i[0], i[1], i[2], i[3]))
                else:
                    print("{0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
            # print(ai_score)
            print("Score | User :{user} | AI :{ai}".format(user = user_score, ai = ai_score))
            if user_score > ai_score:
                print("user win !")
            elif ai_score > user_score:
                print("ai win !")
            else:
                user_remaining = []
                for id_row, row in enumerate(user_board):
                    for id_col, col in enumerate(row):
                        if user_board[id_row][id_col] in total_chess:
                            user_remaining.append(user_board[id_row][id_col])

                ai_remaining = []
                for id_row, row in enumerate(ai_board):
                    for id_col, col in enumerate(row):
                        if ai_board[id_row][id_col] in total_chess:
                            ai_remaining.append(ai_board[id_row][id_col])

                user_max = max(user_remaining)
                ai_max = max(ai_remaining)
                if user_max > ai_max:
                    print("user win !")
                elif ai_max > user_max:
                    print("ai win !")
                else:
                    print("tie game !")
            playing_game = False 


# function for check-and-mark
def check_and_mark(board):
    # print("~~~~~")
    # total_chess = [2, 3, 5, 8, 13]
    
    mark_board = copy.deepcopy(board)
    for id_row, row in enumerate(board):
        for id_col, col in enumerate(row):
            # if board[id_row][id_col] != "X" and board[id_row][id_col] != 0:\
            # print("now checking :", id_row, id_col)
            if board[id_row][id_col] in set(total_chess):
                #corner
                if (id_row, id_col) == (0, 0):
                    value = check_corner(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"
                            
                elif (id_row, id_col) == (len(board) - 1, 0):
                    value = check_corner(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"

                elif (id_row, id_col) == (0, len(board) - 1):
                    value = check_corner(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"

                elif (id_row, id_col) == (len(board) - 1, len(board) - 1):
                    value = check_corner(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"

                #side between corner
                elif 0 < id_row < (len(board) - 1) and id_col == 0:
                    value = check_side(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"

                elif id_row == 0 and 0 < id_col < (len(board) - 1):
                    value = check_side(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"

                elif 0 < id_row < (len(board) - 1) and id_col == (len(board) - 1):
                    value = check_side(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"

                elif id_row == (len(board) - 1) and 0 < id_col < (len(board) - 1):
                    value = check_side(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"
                # inside 
                elif 0 < id_row < (len(board) - 1) and 0 < id_col < (len(board) - 1):
                    value = check_inside(id_row, id_col, board)
                    if value > 15:
                        # print("remove", board[id_row][id_col])
                        mark_board[id_row][id_col] = "X"
                # print("value :", value)
    # print("starting remove")
    # remove
    for id_row, row in enumerate(mark_board):
        for id_col, col in enumerate(row):
            if mark_board[id_row][id_col] == "X":
                board[id_row][id_col] = "X"

    return board


def check_corner(id_row, id_col, board):
    if (id_row, id_col) == (0, 0):
        neibor_1 = (board[id_row][id_col+1] if board[id_row][id_col+1] != "X" else 0)
        neibor_2 = (board[id_row+1][id_col] if board[id_row+1][id_col] != "X" else 0)
        neibor_3 = (board[id_row+1][id_col+1] if board[id_row+1][id_col+1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3
        # print(value)
        return int(value)
    elif (id_row, id_col) == (len(board) - 1, 0):
        neibor_1 = (board[id_row][id_col+1] if board[id_row][id_col+1] != "X" else 0)
        neibor_2 = (board[id_row-1][id_col] if board[id_row-1][id_col] != "X" else 0)
        neibor_3 = (board[id_row-1][id_col+1] if board[id_row-1][id_col+1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3
        # print(value)
        return int(value)
    elif (id_row, id_col) == (0, len(board) - 1):
        neibor_1 = (board[id_row][id_col-1] if board[id_row][id_col-1] != "X" else 0)
        neibor_2 = (board[id_row+1][id_col] if board[id_row+1][id_col] != "X" else 0)
        neibor_3 = (board[id_row+1][id_col-1] if board[id_row+1][id_col-1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3
        # print(value)
        return int(value)
    elif (id_row, id_col) == (len(board) - 1, len(board) - 1):
        neibor_1 = (board[id_row][id_col-1] if board[id_row][id_col-1] != "X" else 0)
        neibor_2 = (board[id_row-1][id_col] if board[id_row-1][id_col] != "X" else 0)
        neibor_3 = (board[id_row-1][id_col-1] if board[id_row-1][id_col-1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3
        # print(value)
        return int(value)

def check_side(id_row, id_col, board):
    if 0 < id_row < (len(board) - 1) and id_col == 0 :
        neibor_1 = (board[id_row-1][id_col] if board[id_row-1][id_col] != "X" else 0)
        neibor_2 = (board[id_row+1][id_col] if board[id_row+1][id_col] != "X" else 0)
        neibor_3 = (board[id_row-1][id_col+1] if board[id_row-1][id_col+1] != "X" else 0)
        neibor_4 = (board[id_row][id_col+1] if board[id_row][id_col+1] != "X" else 0)
        neibor_5 = (board[id_row+1][id_col+1] if board[id_row+1][id_col+1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3 + neibor_4 + neibor_5
        return int(value)
    elif id_row == 0 and 0 < id_col < (len(board) - 1) :
        neibor_1 = (board[id_row][id_col-1] if board[id_row][id_col-1] != "X" else 0)
        neibor_2 = (board[id_row][id_col+1] if board[id_row][id_col+1] != "X" else 0)
        neibor_3 = (board[id_row+1][id_col-1] if board[id_row+1][id_col-1] != "X" else 0)
        neibor_4 = (board[id_row+1][id_col] if board[id_row+1][id_col] != "X" else 0)
        neibor_5 = (board[id_row+1][id_col+1] if board[id_row+1][id_col+1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3 + neibor_4 + neibor_5
        return int(value)
    elif 0 < id_row < (len(board) - 1) and id_col == (len(board) - 1) :
        neibor_1 = (board[id_row-1][id_col-1] if board[id_row-1][id_col-1] != "X" else 0)
        neibor_2 = (board[id_row][id_col-1] if board[id_row][id_col-1] != "X" else 0)
        neibor_3 = (board[id_row+1][id_col-1] if board[id_row+1][id_col-1] != "X" else 0)
        neibor_4 = (board[id_row-1][id_col] if board[id_row-1][id_col] != "X" else 0)
        neibor_5 = (board[id_row+1][id_col] if board[id_row+1][id_col] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3 + neibor_4 + neibor_5
        return int(value)
    elif id_row == (len(board) - 1) and 0 < id_col < (len(board) - 1) :
        neibor_1 = (board[id_row][id_col-1] if board[id_row][id_col-1] != "X" else 0)
        neibor_2 = (board[id_row][id_col+1] if board[id_row][id_col+1] != "X" else 0)
        neibor_3 = (board[id_row-1][id_col-1] if board[id_row-1][id_col-1] != "X" else 0)
        neibor_4 = (board[id_row-1][id_col] if board[id_row-1][id_col] != "X" else 0)
        neibor_5 = (board[id_row-1][id_col+1] if board[id_row-1][id_col+1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3 + neibor_4 + neibor_5
        return int(value)

def check_inside(id_row, id_col, board):
    if 0 < id_row < (len(board) - 1) and 0 < id_col < (len(board) - 1):
        neibor_1 = (board[id_row-1][id_col-1] if board[id_row-1][id_col-1] != "X" else 0)
        neibor_2 = (board[id_row-1][id_col] if board[id_row-1][id_col] != "X" else 0)
        neibor_3 = (board[id_row-1][id_col+1] if board[id_row-1][id_col+1] != "X" else 0)
        neibor_4 = (board[id_row][id_col-1] if board[id_row][id_col-1] != "X" else 0)
        neibor_5 = (board[id_row][id_col+1] if board[id_row][id_col+1] != "X" else 0)
        neibor_6 = (board[id_row+1][id_col-1] if board[id_row+1][id_col-1] != "X" else 0)
        neibor_7 = (board[id_row+1][id_col] if board[id_row+1][id_col] != "X" else 0)
        neibor_8 = (board[id_row+1][id_col+1] if board[id_row+1][id_col+1] != "X" else 0)
        value = board[id_row][id_col] + neibor_1 + neibor_2 + neibor_3 + neibor_4 + neibor_5 + neibor_6 + neibor_7 + neibor_8
        return int(value)

def compute_score(board, checked_board):
    total_chess = [2, 3, 5, 8, 13]
    # update marking in checked board
    for id_row, row in enumerate(board):
        for id_col, col in enumerate(row):
            if board[id_row][id_col] == "X":
                checked_board[id_row][id_col] = "X"
    # compute score
    score = 0
    for id_row, row in enumerate(checked_board):
        for id_col, col in enumerate(row):
            if checked_board[id_row][id_col] in set(total_chess):
                score += checked_board[id_row][id_col]
    return score
# function for AI play
def AI_move(board, ai_board, user_board, AI_chess):
    move_list = []
    for id_row, row in enumerate(board):
        for id_col, col in enumerate(row):
            if board[id_row][id_col] == 0:
                move_list.append([id_row, id_col])

    best_ratio = 0
    best_move = []

    for id_row, id_col in move_list:
        for ai_weight in AI_chess:
            simulated_board = copy.deepcopy(board)
            simulated_ai_board = copy.deepcopy(ai_board)
            simulated_user_board = copy.deepcopy(user_board)

            # card_idx = AI_chess.index(ai_weight)
            # AI_chess.pop(card_idx)
            simulated_board[id_row][id_col] = ai_weight
            simulated_ai_board[id_row][id_col] = ai_weight 

            simulated_board = check_and_mark(simulated_board)

            # print('\n'.join(' '.join(str(cell) for cell in row) for row in simulated_board)) 
            # print("="*20)
            ai_score = compute_score(simulated_board, simulated_ai_board)
            user_score = compute_score(simulated_board, simulated_user_board)
            ratio = (ai_score - user_score)/ai_weight
            if ratio > best_ratio:
                best_ratio = ratio
                best_move = [id_row, id_col, ai_weight]

    if best_move == []:
        idx = choice(move_list)
        value = choice(AI_chess)
    else:
        idx = best_move[0:2]
        value = best_move[2]

    # print("best ratio :", best_ratio)
    # print("best move :", best_move)
    
    # print("idx, value :", idx, value)
    return idx[0], idx[1], value


if user_first == "y":
    user_play_first(playing_game, board, User_chess, AI_chess)
else:
    ai_play_first(playing_game, board, User_chess, AI_chess)
