import random
num = random.randint(1,100)
i = 1
while True:
  guess = int(input("Guess The Number(1 to 100):"))
  if guess == num:
    print(f"Correct Guess\n The number is {num}")
    print(f"You took {i} guesses")
    break
  elif guess > num:
    print("The number is smaller. Guess again\n")
    i = i + 1
  else: 
    print("The number is Larger. Guess again\n")
    i = i + 1

  