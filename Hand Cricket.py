import random
import pyautogui
import os
import time
# def screenshot():
#     screenshot = pyautogui.screenshot()
#     screenshot.save(r"C:\Users\ARSHAD\Desktop\pic1.png")

def colour():
    os.system('color 10')
    time.sleep(0.2)
    os.system('color 91')
    time.sleep(0.2)
    os.system('color 81')
    time.sleep(0.2)
    os.system('color 17')
    time.sleep(0.2)
    os.system('color 16')
    time.sleep(0.2)
    os.system('color 17')
    time.sleep(0.2)
    os.system('color 51')
    time.sleep(0.2)
    os.system('color 14')
    time.sleep(0.2)
    os.system('color 07')
    time.sleep(0.2)

print("\n\n*****    Hey Man!!!!!! \nWELCOME TO ARSHAD'S GAMING...    *****")
def game():
    print("\nNOTE : Enter a number between 0 - 10. System will select a random number between 1 - 10.\nIf the number chosen by you and number chosen by system are same, Then the game will END ")
    score = 0
    com_score = 0
    while True:
        comp_run = random.randrange(1, 11)
        print(comp_run)
        try:
            your_run = int(input("\n\nEnter Your Run : "))
        except ValueError:
            print("You shoud Enter Run. \nIf You haven't entered any Run then the Your run will be considered as 0")
            your_run = 0
        if your_run > 10:
            print("\n***  Invalid RUN , the run should be between 1 to 10 ***")
            
        elif your_run != comp_run:
            score = score + your_run
            com_score = com_score + comp_run
            print("\n$$$   Computer Has Chosen : ",comp_run,"    $$$")
            print("\n----   Computer Score Is : ",com_score,"   ----")
            print("----   Your Score Is : ",score,"   ----")
            print("____   Continue Playing   ____")
        else:
            print("\n$$$   Computer Has Chosen : ",comp_run,"    $$$")
            print("\n****   GAME END (Your Run matches with Computer's Run)   ****")
            print("         Computer Score Is : ", com_score)
            print("         Your Score Is : ", score)
            break

    if score > com_score:
        print("\n////    Congradulations!!!!!!!!!!!!!!!!!!\n        You Had WON!!!!!!!!!!!!!!!!!!    ////")
        colour()
        
    elif score == com_score:
        print("\n////    Scores are equal...\n        This Match Has Tired...     ////")
        colour()
        
    else:
        print("\n////    OH NOO!!!!\n        You LOST this math... Computer has won this match...    ////")
        colour()
        

game()
while True:
    try:
        choise = int(input("\n\n\n Enter 100 to play again OR Enter 0 to quit the Game : "))
    except ValueError:
        print(" PLEASE Enter a Choise")
        choise = 12
    if choise == 100:
        game()
    elif choise == 0:
        break
    else:
        print("\n ... Enter either 100 to CONTINUE or 0 to QUIT ...")