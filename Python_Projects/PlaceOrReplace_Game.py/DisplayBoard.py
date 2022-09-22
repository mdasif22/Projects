
#HERE IS ONE OF THE TIMEPASS GAME
#SELECT A POSITION TO PLACE SOME STRING IN THE LIST
#IT WILL DISPLAY YOU NOW THE UPDATED LIST
#YOU CAN DO IT AS MANY TIME AS YOU WANT TO SPEND YOUR TIME

#DISPLAY LIST
row=[0,1,2]
def display_game( row1):
    print("\n!!!  HERE IS THE CURRENT LIST !!!")
    print(row1)
    
#GETTING POSITION  
def position_choice():
    choice = "wrong"
    while choice not in ['0','1','2']:
        choice = input("\nENTER THE POSITION [0,1,2] \n")
        
        if choice not in ['0','1','2']:
            print("\n!! INVALID CHOICE!!")
    return int(choice)


#PLACING OR REPLACING STRING
def replacement(row,position_choice):
    
    user_pos = input("\nENTER THE STRING TO PLACE OR REPLACE \n")
    row[position_choice] = user_pos
    return row

#ASKING TO PLAY AGAIN?
def game_on():
    choice = "wrong"
    while choice not in ['Y','N']:
        choice = input("\nKEEP PLAYING ? [ Y | N ] \n")
        
        if choice not in ['Y','N']:
            print("\n!!PLEASE ENTER VALID OPTION!!")
        
    if choice == 'Y':
        return True
    else:
        return False
    
#CALLING ALL FUNCTIONS
gameon_choice = True
row=[0,1,2]
while gameon_choice==True:
    display_game(row)
    position = position_choice()
    row= replacement(row,position)
    display_game(row)
    gameon_choice = game_on()

