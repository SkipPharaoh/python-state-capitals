from capitals import states
import random

print("Hello there! Welcome to my game that will test your knowledge of state capitals. Simply enter the capital for each state prompt. A score will be provided at the end and to stop playing, just type exit")

def game():
    random.shuffle(states)
    score = 0
    
    for i in states:
        
        name = i['name']
        capital = i['capital']

        answer = input(f"{name}:  Have any guess for this state's capital? ")

        if answer == capital:
            score += 1 
            print(f"Correct! Your score is: ", score)
        elif answer == 'exit':
            break
        else:
            print(f"Incorrect. Your score is: ", score)

    if score == 50:
        print("Winner Winner, Chicken Dinner! Thanks for playing")
    elif answer == 'exit':
        print('Sorry to see you go! Please play again')
    else:
        print("Good Try, want to try again?")

game()