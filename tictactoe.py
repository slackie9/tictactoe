import os
os.system("clear")

class Board:
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]


    def display(self):
        
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        print("\n")
    
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):

        for combo in [[1,2,3], [4,5,6],[7,8,9],[1,4,7],[2,5,8], [3,6,9],[1,5,9],[3,5,7] ]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result == True:
                return True
       
        return False

    def is_tie(self):
        used_cells =0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
         self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def ai_move(self, player):
        if player == "X":
            enemy = "O"
        if player =="O":
            enemy = "X"
        # if the center is open, choose that
        if self.cells[5] == " ":
            self.update_cell(5, player)
            
        # AI can win
        # AI Blocks
        # Choose Random
        for i in range(1,9):
            if self.cells[i] == " ":
                self.update_cell(i,player)
                break

            

def print_header():
    print("Welcome to Tic-Tac-Toe \n")
    
def refresh_screen():
    os.system("clear")
    print_header()
    board.display()


board = Board()                   
while True:
    refresh_screen()

    # get X sign
    x_choice = int(input("\n X Please choose 1 - 9. > "))

    #update board
    board.update_cell(x_choice, "X")
    refresh_screen()

    # Check for an X win
    if board.is_winner("X"):
        print("\n X wins ! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
    # Check for an Tie
    if board.is_tie():
        print("\n Tie ! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
    # get O sign
    #x_choice = int(input("\n O Please choose 1 - 9. > "))
   
    board.ai_move("O")
    #refersh screen
    refresh_screen()
    #update Board   
    #board.update_cell(x_choice, "O")
    if board.is_winner("O"):
        print("\n O wins ! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
    # Check for an Tie
    if board.is_tie():
        print("\n Tie ! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    

