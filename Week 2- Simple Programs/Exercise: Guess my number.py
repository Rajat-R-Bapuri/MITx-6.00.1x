print("Please think of a number between 0 and 100!")
l = 0
h = 100
while(True):
    guess = int((l + h) / 2)
    print("Is your secret number " + str(int(guess)) + "?")
    reply = input("Enter 'h' to indicate the guess is too high. Enter 'l'\
              to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(reply == 'c'):
        break
    elif(reply == 'h'):
        h = guess
    elif(reply == 'l'):
        l = guess
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(guess))
        
