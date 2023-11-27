import random
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: # negative number ain't a digit
        print("Pls type a number larger than 0 next time.")
        quit()
else:
    print("Pls type a number next time.")
    quit()

random_number = random.randint(0,top_of_range) #include top_of_range
guess_numb = 0
while True:
    guess_numb += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Pls type a number next time.")
        continue
    if guess == random_number:
        print("U got it!")
        break
    elif guess < random_number:
        print("U're below the number")
    else:
        print("U're avobe the number")

print(f'U guessed it in {guess_numb} guesses.')
