board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
place = []
for key in board:
    place.append(key)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def gamestart():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(board)
        print("It is now your turn," + turn + ".Where would you like to move?")
        move = input()
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Hey! That spots taken! \nWhere will you go instead?")
            continue
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGaaameOver!\n")
                print(" **** " + turn + " won the game! ****")
                break
        if count == 9:
            print("\nGaaameOver!\n")
            print("It's a Tie dude!")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Rematch? (y/n)")
    if restart == "y" or restart == "Y":
        for key in place:
            board[key] = " "
        gamestart()
if __name__ == "__main__":
    gamestart()