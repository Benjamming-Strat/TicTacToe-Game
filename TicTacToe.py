# Program fpr TicTacToe-Game


# Class for Board
class Board:
    def __init__(self):
        self.board_list = [0 for x in range(9)]             #list comprehension for 0 * 9
        #[0,0,0,0,0,0,0,0,0,0]
        #[1,]



    def make_turn(self, cell, Player):             
        if self.is_valid(cell):                       #writes player sign( 1 or 2) into board_list
            self.board_list[cell] = Player.symbol
            return True
        else:
            False

        #looping through elemets in board_lsit and checking  all values switched from 0 to 1 or 2,  not return false, false=> not full
    def is_full(self):
        for i in range(9):     # it loops to the next entry of 0, when it reaches i=0, loop stops and as long as there is a stop due to an input it will not go to the return True
                    
            if self.board_list[i] == 0:
                return False
        
        return True

    def is_valid(self, cell): # checks move was a valid move otherwise returns False
        if self.board_list[cell] == 0:
            return True
        else:
            return False


    #function to print the right sign to the board
    def print_sign_to_board(self,sign):        #sign = self.board_list[0] = Liste[0,0,0,0,0,0,0,0,0,0]
        #sign = sign
        if sign== 1:
            return "X"
        elif sign == 0:
            return " "
        else:
            return "O"      



    #function for Boardprint
    def print_board(self):
        print ( " " + self.print_sign_to_board(self.board_list[0]) + " | "+ self.print_sign_to_board(self.board_list[1]) + " | "+ self.print_sign_to_board(self.board_list[2]) + "\n" +   #giving self.board_list as parameter to function print_sign_to_board as Sign
                " " + self.print_sign_to_board(self.board_list[3]) + " | "+ self.print_sign_to_board(self.board_list[4]) + " | "+ self.print_sign_to_board(self.board_list[5]) + "\n" +
                " " + self.print_sign_to_board(self.board_list[6]) + " | "+ self.print_sign_to_board(self.board_list[7]) + " | "+ self.print_sign_to_board(self.board_list[8]))




    #checking if there are 3 of the same sign in the same row, column or diagonal that lead to win
    def check_3_in_a_row(self, Player):
        sign = Player.symbol
        #rows left to right
        if self.board_list[0] == sign and  self.board_list[1] and  self.board_list[2]==sign:
            return True
        elif self.board_list[3] == sign and  self.board_list[4] and  self.board_list[5]==sign:
            return True
        elif self.board_list[6] == sign and  self.board_list[7] and  self.board_list[8]==sign:
            return True

        #columns    
        elif self.board_list[0] == sign and  self.board_list[3] and  self.board_list[6]==sign:
            return True
        elif self.board_list[1] == sign and  self.board_list[4] and  self.board_list[7]==sign:
            return True
        elif self.board_list[2] == sign and  self.board_list[5] and  self.board_list[8]==sign:
            return True        

         #diagonal   
        elif self.board_list[0] == sign and  self.board_list[4]==sign and  self.board_list[8]==sign:
            return True
        elif self.board_list[2] == sign and  self.board_list[4]==sign and  self.board_list[6]==sign:
            return True






class Player:
    def __init__(self, symbol):
        self.symbol = symbol

if __name__=="__main__":

    board = Board()
    board1 = Board()
    player_a = Player(1)        #in function print_sign_to_board is defined what symbol we need as input 1=X, not 0 = O
    palyer_b = Player(2)
    active_player = player_a 
    while not board.is_full():              #while is_full == False, keep looping
        board.print_board()
               #player_a starts always
        print("geht los")
        try:
            cell = int(input("Please chose where to place your sign (1-9)"))            #cast cell into integer
            
        except ValueError:
            continue

        cell = cell - 1
        print("#######################################################")

        if cell < 0 or cell > 9:            #checks  cell i in the board range
            print("pleasae chose a number between 1 and 9")
            print()
            continue
        
        if not board.make_turn(cell,active_player):     #if make_turn==False becuase is_valid() is False / is_valid checks if there is already a sign
            print("invalid move")
            print()
            continue

        if board.check_3_in_a_row(active_player):
            print("Player %s, you have won - congrats"%(active_player.symbol))
        

        if active_player==player_a:     #switching the players
            active_player=palyer_b
        else:
            active_player=player_a   

        

        




    


