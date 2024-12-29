import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print(''+ format_symbol(board[0]) + '|'+ format_symbol(board[1]) + '|' + format_symbol(board[2]))
    print(Fore.CYAN + '------')
    print(''+ format_symbol(board[3]) + '|'+ format_symbol(board[4]) + '|' + format_symbol(board[5]))
    print(Fore.CYAN + '------')
    print(''+ format_symbol(board[6]) + '|'+ format_symbol(board[7]) + '|' + format_symbol(board[8]))

def format_symbol(symbol):
    if symbol == 'X':
        return Fore.BLUE + symbol + Fore.RESET
    elif symbol == 'O':
        return Fore.RED + symbol + Fore.RESET
    else:
        return Fore.YELLOW + symbol + Fore.RESET
    
def playerchoice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.LIGHTMAGENTA_EX + 'Do you want x or o').upper()
        if symbol == 'X':
            return('X', 'O')
        else:
            return('O', 'X')

def playermove(board, symbol, player_name):
    move = -1
    while move not in range(1,10) or not board[move-1].isdigit():
        try:
            move = int(input(Fore.GREEN + f'{player_name}, enter your move(1,9)'))
            if move not in range(1,10) or not board[move-1].isdigit():
                print(Fore.RED + "invalid move, please try again") 
        except ValueError:
            print(Fore.CYAN + "Enter a number between 1 and 9")
    board[move-1] = symbol 

def aimove(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = ai_symbol
            if check_win(boardcopy, ai_symbol):
                board[i] = ai_symbol
                return 
            
    
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = player_symbol
            if check_win(boardcopy, player_symbol):
                board[i] = player_symbol
                return
            
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
    for c in win_conditions:
        if board[c[0]] == board[c[1]] == board[c[2]] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board) 

def tictactoe():
    print(Fore.LIGHTWHITE_EX + 'Welcome to Tictactoe')
    player_name = input(Fore.LIGHTGREEN_EX + 'Please enter your name')
    while True:
        board = ['1','2','3','4','5','6','7','8','9']
        player_symbol, ai_symbol = playerchoice()
        turn = 'Player'
        game_on = True
        while game_on: 
            display_board(board)
            if turn == 'Player':
                playermove(board, player_symbol, player_name)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.LIGHTBLUE_EX + f"Congrats {player_name}, you've won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(Fore.WHITE + "It's a tie")
                        break 
                    else:
                        turn = 'AI' 
            else:
                print(Fore.LIGHTCYAN_EX + "The AI is making it's move...")
                aimove(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.LIGHTGREEN_EX + "AI has won the game")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(Fore.WHITE + "It's a tie")
                        break 
                    else:
                        turn = 'Player'
        play_again = input(Fore.LIGHTMAGENTA_EX + f"{player_name}, Do you want to play again(Y/N)").lower()
        if play_again != 'yes':
            print(Fore.CYAN + 'Thank you for playing')
            break

if __name__ == "__main__":
    tictactoe()

