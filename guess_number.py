import random
number = random.randint(1,10)
player_name = input("Enter Your Name : ")
print("Hi ! "+player_name+", Now I'll Guess a Number Between 1 to 10..")
num_of_guesses = 0

while num_of_guesses < 5:
    guess = int(input("Enter Any Number from 1 to 10 : "))
    num_of_guesses+=1
    if guess < number:
        print("You have guessed a Lower number")
    if guess > number:
        print("You have guessed a Higher number")
    if guess == number:        
        print("Congrats !, Your Guess is Correct")
        break
if guess == number:
    print("you have guessed the number in"+ str(num_of_guesses())+"tries")
else :
    print("You did not Guess the Number, The number is "+str(number))