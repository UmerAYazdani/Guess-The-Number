#Lets the program generate at random.
import random

#Picks and stores a random number chosen within the range of 1-10 within the "randomNumber" variable.
randomNumber = random.randint(1,10)

#Lets the user input a Guess, and it stores that guess in the "guess" variable.
guess = int(input("Guess the number between 1-10:"))
guesses = 0
#An if/else loop 
while randomNumber != guess: 
  #if number is less then, then a hint will be displayed.
  if guess < randomNumber:
   print("Hint: Guessed number is too low.")
   guess = int(input("Guess the number between 1-10:"))
 #if number is to high display another hint.
  elif guess > randomNumber:
   print("Hint: Number guessed number is too high")
   guess = int(input("Guess the number between 1-10:"))
  guesses+=1


#When correct number is guessed it will diplayed :correct and the program will end.
print("Correct! You took", guesses,"tries.") 

  

