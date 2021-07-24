

print("\n\n------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                              Tic Tak Toe                                                                       ")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#  Firstly selecting the  signs of the players

def select_sign():
    player1_sign = ""
    player2_sign = ""

    while player1_sign != 'x' or player1_sign != 'o':
        player1_sign = input("\nSelect your sign from ('x' or 'o') : ")
        if player1_sign == "x" or player1_sign == 'o':
            break
        else:
            print("\n please enter the correct sign ")
        
  
    if player1_sign == 'x':
        player2_sign = 'o'
            
            
    else:
        player2_sign = 'x'
            

    return (player1_sign,player2_sign)








# Selecting the players turn
def select_turn():
    while(1):
        choice =int(input("\nWhich player wants to go first (1 or 2): "))
        player1_sign =""
        player2_sign =""

        if choice == 1:
            ply = 0
            break
        elif choice == 2:
            ply = 1
            break
        
        else:
            print("Invalid choice !!")
    
    player1_sign,player2_sign = select_sign()   

    print("\nThe player1 selected : ",player1_sign)
    print("The player2 selected : ",player2_sign)

    players_sign = [player1_sign,player2_sign]

    return ply,players_sign

player_turn, players_sign = select_turn();  






# main game logic
def check_win(currentPlayer,row1,row2,row3,row4,row5,row6,row7,row8):

    win =False

    #checking from 1 1 cell
    if row2[1] == row2[3] and row2[3] == row2[5]:
        if row2[1] != " " and row2[3] != " " and row2[5] != " ":
           win = True
      
    elif row2[1] == row5[1] and row5[1] == row8[1]:
       if row2[1] != " " and row5[1] != " " and row8[1] != " ":
           win = True

    elif row2[1] == row5[3] and row5[3] == row8[5]:
        if row2[1] != " " and row5[3] != " " and row8[5] != " ":
           win = True 

    elif row8[1] == row8[3] and  row8[3] == row8[5]:
        if row8[1] != " " and row8[3] != " " and row8[5] != " ":
           win = True

    elif row2[5] == row5[5] and row5[5] == row8[5]:
        if row2[5] != " " and row5[5] != " " and row8[5] != " ":
           win = True
    
    elif row2[3] == row5[3] and row5[3] == row8[3]:
        if row2[3] != " " and row5[3] != " " and row8[3] != " ":
           win = True

    elif row5[1] == row5[3] and row5[3] == row5[5]:
        if row5[1] != " " and row5[3] != " " and row5[5] != " ":
           win = True

    elif row8[1] == row5[3] and row5[3] == row2[5]:
        if row8[1] != " " and row5[3] != " " and row2[5] != " ":
           win = True

    else:
        print()
    

    return win













# Game input
def game_logic(currentPlayer,players_sign,row1,row2,row3,row4,row5,row6,row7,row8):
    
    check = True
    
    while(check):
        print("\n\n---------------------------------------------------------------------------------")
        print("Player " + str(currentPlayer+1) + " turn : ")
        print("---------------------------------------------------------------------------------")


        print("\n")
        print("   1 | 2 | 3  ")
        print("_ _ _|_ _|_ _ _")
        print("     |   |    ")
        print("   4 | 5 | 6 ")
        print("_ _ _|_ _|_ _ _")
        print("     |   |    ")
        print("   7 | 8 | 9 ")
        
        position = int(input("\nPlease select the position with referce to the above table : "))
        
        if position in (1,2,3):
            if position == 1:
                if row2[1] == " ":
                    row2[1] = players_sign[currentPlayer]
            
            elif position == 2:
                if row2[3] == " ":
                    row2[3] = players_sign[currentPlayer]

            else:
                if row2[5] == " ":
                     row2[5] = players_sign[currentPlayer]
        

        elif position in (4,5,6):
            if position == 4:
                if row5[1] == " ":
                     row5[1] = players_sign[currentPlayer]
            
            elif position == 5:
                if row5[3] == " ":
                    row5[3] = players_sign[currentPlayer]

            else:
                if row5[5] == " ":
                   row5[5] = players_sign[currentPlayer]


        elif position in (7,8,9):
            if position == 7:
                if row8[1] == " ":
                   row8[1] = players_sign[currentPlayer]
            
            elif position == 8:
                if row8[3] == " ":
                   row8[3] = players_sign[currentPlayer]

            else:
                if row8[5] == " ":
                   row8[5] = players_sign[currentPlayer]
        else:
            print("\n Invalid Input")

        
        print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
        print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
        print(row4[0],row4[1],row4[2],row4[3],row4[4],row4[5],row4[6])
        print(row5[0],row5[1],row5[2],row5[3],row5[4],row5[5],row5[6])
        print(row6[0],row6[1],row6[2],row6[3],row6[4],row6[5],row6[6])
        print(row7[0],row7[1],row7[2],row7[3],row7[4],row7[5],row7[6])
        print(row8[0],row8[1],row8[2],row8[3],row8[4],row8[5],row8[6])

       
        CHECK = check_win(currentPlayer,row1,row2,row3,row4,row5,row6,row7,row8)

        if CHECK == True:
            print("\nThe player " + str(currentPlayer+1) + " is win !! 🏆")
            print("\n\n")
            break
        
        if row2[1]!=" " and row2[3]!=" " and row2[5]!=" "and row5[1]!=" " and row5[3]!=" " and row5[5]!=" " and row8[1]!=" " and row8[3]!=" " and row8[5]!=" ":
            print("Game Draw !! 😁")
            print("\n\n")
            break




        # Altering the player
       
        if currentPlayer == 0:
            currentPlayer = 1
        else:
            currentPlayer = 0
        


row1 = [" "," "," | "," "," | "," "," "]
row2 = [" "," "," | "," "," | "," "," "]
row3 = ["_","_","_|_","_","_|_","_","_"]
row4 = [" "," "," | "," "," | "," "," "]
row5 = [" "," "," | "," "," | "," "," "]
row6 = ["_","_","_|_","_","_|_","_","_"]
row7 = [" "," "," | "," "," | "," "," "]
row8 = [" "," "," | "," "," | "," "," "]

game_logic(player_turn,players_sign,row1,row2,row3,row4,row5,row6,row7,row8)
play_again = input("Do you want to play again (y or n) : ")



# Play again code
if play_again == 'y':
    row1 = [" "," "," | "," "," | "," "," "]
    row2 = [" "," "," | "," "," | "," "," "]
    row3 = ["_","_","_|_","_","_|_","_","_"]
    row4 = [" "," "," | "," "," | "," "," "]
    row5 = [" "," "," | "," "," | "," "," "]
    row6 = ["_","_","_|_","_","_|_","_","_"]
    row7 = [" "," "," | "," "," | "," "," "]
    row8 = [" "," "," | "," "," | "," "," "]

    game_logic(player_turn,players_sign,row1,row2,row3,row4,row5,row6,row7,row8)

else:
    print("Thanks for Playing 😊")



    