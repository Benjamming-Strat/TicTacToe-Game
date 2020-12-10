class Board():
    def __init__(self):
        self.board_list = [0 for x in range(9)]

    def print_board(self):

           print(
            self.print_to_board(self.board_list[0]) + " | " + self.print_to_board(self.board_list[1]) + " | " +self.print_to_board(self.board_list[2]) + "\n" +
            self.print_to_board(self.board_list[3]) + " | " + self.print_to_board(self.board_list[4]) + " | " +self.print_to_board(self.board_list[5]) + "\n"+
            self.print_to_board(self.board_list[6]) + " | " + self.print_to_board(self.board_list[7]) + " | " +self.print_to_board(self.board_list[8])
           )

  
    def print_to_board(self,sign):
        if sign == 1:
            return "X"
        elif sign != 1 and sign != 0:
            return "O"
        elif sign == 0:
            return " "

    def sign_to_board_list(self,cell, Player):
        if self.is_valid(cell):
            self.board_list[cell] = Player.symbol
            return True
        return False
        

    def is_full(self):
        for i in range(len(self.board_list)):          
            if self.board_list[i] == 0:
                
                return False
        return True
    
    def check_win(self, Player):
        sign=Player.symbol
        #horizontal win
        if self.board_list[0]== sign  and self.board_list[1]==sign and self.board_list[2]==sign:
            return True
        elif self.board_list[3]== sign  and self.board_list[4]==sign and self.board_list[5]==sign:
            return True
        elif self.board_list[6]== sign  and self.board_list[7]==sign and self.board_list[8]==sign:
            return True
        #verticalwin
        elif self.board_list[0]== sign  and self.board_list[3]==sign and self.board_list[6]==sign:
            return True
        elif self.board_list[1]== sign  and self.board_list[5]==sign and self.board_list[7]==sign:
            return True
        elif self.board_list[2]== sign  and self.board_list[5]==sign and self.board_list[8]==sign:
            return True
        #diagonal
        elif self.board_list[0]==sign and self.board_list[4]==sign and self.board_list[8]==sign:
            return True
        elif self.board_list[2]==sign and self.board_list[4]==sign and self.board_list[6]==sign:
            return True
        


    def is_valid(self, cell):
        if self.board_list[cell] == 0:
            return True
        else:
            return False


class Player():
    def __init__(self, symbol):
        self.symbol = symbol


if __name__=="__main__":

    board1 = Board()
    player_a = Player(1)
    player_b = Player(2)
    active_player = player_a
   

    while not board1.is_full():
        print("now it's player %s's move\nxxxxxxxxxxxxxxxxxxxxxxxx" %(active_player.symbol))
        board1.print_board()
        try:
            cell = int(input("Please Chose a field to place your sign from 1 to 9: \n"))
            
            
        except ValueError:
            print("Please chose a real number!\n\n")
            continue

        cell -= 1
        
        if cell < 0 or cell > 8:
            print("Please chose a number between 1 and 9")
            continue
        

        if not board1.sign_to_board_list(cell, active_player):
            print("invalid move")
            continue 
        

        if board1.check_win(active_player):
            board1.print_board()
            print("Congrats Player%s, you have won!!!"%(active_player.symbol))
            break

        if active_player==player_a:
            active_player=player_b
        else:
            active_player=player_a
        
        

        

        
