import random

def _new_board():
    """Create new game board."""
    board = []
    for square in range(9):
        board.append(" ")
    return board



def _display_board(board):
    """Display game board on screen."""
    print "\n\t", board[0], "|", board[1], "|", board[2]
    print "\t","---------"
    print "\t",board[3], "|", board[4], "|", board[5]
    print "\t","---------"
    print "\t",board[6], "|", board[7], "|", board[8]
    return board



def _moves(board):
    valid_moves = []
    for pos in range(len(board)):
        if board[pos]==" ":
            valid_moves.append(pos)
    return valid_moves




def _playerInput(board):
    moves = _moves(board)
    print moves
    while True:
        choice = int(raw_input("Make your move from these valid positions " + str(moves) + ":"))
        if choice not in moves:
            print "Try again..Enter a valid position"
            continue
        else:
            board[choice]="X"
            break



def _cpuInput(board):
    cpu_choice  = (random.choice(_moves(board)))
    board[cpu_choice]="O"





def _checkWinner(board,marker):
    if (board[0]==board[1]==board[2]==marker or \
        board[3]==board[4]==board[5]==marker or \
        board[6]==board[7]==board[8]==marker or \
        board[0]==board[3]==board[6]==marker or \
        board[1]==board[4]==board[7]==marker or \
        board[2]==board[5]==board[8]==marker or \
        board[0]==board[4]==board[8]==marker or \
        board[2]==board[4]==board[6]==marker):
        return True
    else :
        return False




def _isBoardFull(board):
    for item in board:
        if item == " ":
            return False
    return True

def _replay():
    inp = raw_input("would you like to play again (y/n):")
    if inp == "y":
        return True
    else:
        return False



if __name__ == "__main__":
    print "Welcome to the tic tac toe game..!!!"
    while True:
        """Reset the board"""

        board = _new_board()
        _display_board(board)
        gameon = True
        while gameon:
            _cpuInput(board)
            _display_board(board)
            res2 = _checkWinner(board,"O")
            if res2 == True:
                print "cpu wins"
                break
            elif _isBoardFull(board)==True:
                print "its a fukn tie"
                break
                
            _playerInput(board)
            _display_board(board)
            res1 = _checkWinner(board,"X")
            if res1 == True:
                print "player wins"
                break
            elif _isBoardFull(board)==True:
                print "its a fukn tie"
                break




        if not _replay():
            break
