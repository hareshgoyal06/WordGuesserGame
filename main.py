#emblishments contain the following
#1. design elements throughout the code/proper spacing
#2. user cannot guess the same letter twice 
#3. user cannot guess multiple letters at once
#4. user cannot enter a number
#5. User can choose which category they'd like to choose from
import random
restart = True

print('''
 / \--------------------, 
 \_,|                   | 
    |    Word Guesser   | 
    |  ,------------------
    \_/_________________/ 

''')


#intialize functions 
def get_list(ml):
    choice = random.choice(ml)
    return choice
restart = True
def get_option():
  print('''
  Menu Options:
  • Play Again
  • Display Instructions/Play Again
  • Quit 
  ''')
  option = int(input("Select Menu Choice: "))
  if option == 1: 
    return True 
  if option == 2: 
    print('''\nHow to play:  
  Players try and guess all of the letters in a secret word. 
  As they guess correctly, letters are revealed in the secret word. 
  However, players can only guess an incorrect letter five times. 
  If the word is guessed in time, the user wins; if not, they lose.
  ''')
    return True 
  if option == 3:
    return False

def get_category():
  print('''*WORD CATEGORIES*
1. Sports
2. Animals
3. Fruits
  ''')
  while True:
    category = int(input("Please select a category (1, 2, or 3): "))
    if category != 1 and category != 2 and category != 3:
      print("Please enter a valid category! \n")
      continue
    if category == 1:
      return get_list(sports)
    if category == 2:
      return get_list(animals)
    if category == 3:
      return get_list(fruits)

#intialize lists
sports = ["football", "basketball", "tennis", "soccer", "baseball", "golf", "cricket", "hockey", "swimming", "volleyball", "rugby", "boxing", "badminton"]
animals = ["lion", "tiger", "elephant", "giraffe", "monkey", "zebra", "kangaroo", "penguin", "dolphin", "panda"]
fruits = ['apple', 'banana', 'orange', 'kiwi', 'strawberry', 'mango', 'pineapple', 'grapefruit', 'pear', 'watermelon', 'peach', 'blueberry', 'cherry', 'plum', 'lemon']


#main program 
while restart == True:
  print("\n Welcome to Word Guesser!")
  print('''
  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Players try and guess all of the letters in a secret word. 
  As they guess correctly, letters are revealed in the secret word. 
  However, players can only guess an incorrect letter five times. 
  If the word is guessed in time, the user wins; if not, they lose.
  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  ''')
  guess_left = 5
#This segment produces the word to guess
  playword = get_category()
  word = []
  for letter in playword:
      word.append(letter)
  guessed = ["*"]*len(word)
  already_guessed = []
  print("Your word has " + str(len(word)) + " letters. Good luck!\n") 
#This segment codes the part where the user guesses the letters
  while guess_left > 0: 
    guessed_letter = input("Guess a letter " + " ".join(guessed) + " > ").lower()
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("\nPlease enter a single letter.\n")
        continue
    if guessed_letter in already_guessed:
        print("\nYou already guessed that letter.\n")
        continue    
    already_guessed.append(guessed_letter)
    if guessed_letter in word:
      for letter in range(len(word)):
        if guessed_letter == word[letter]:
          guessed[letter] = guessed_letter
      print("\nYou got it!\n")
    if guessed_letter not in word:      
      print("\nNope! Keep Trying!")
      guess_left -= 1 
      print("\nYou have", guess_left, "guesses left!\n")
#if the word is guessed correctly 
    if guessed == word:
      print("Guess a letter " + " ".join(guessed))
      print('''
      -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        You Guessed The Word! Congrats! 
      -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
      ''')      
      restart = get_option()
      if restart == False:
        print("\nThank you for playing!")
        break
      if restart == True:
        guess_left = 5
        playword = get_category()
        word = []
        for letter in playword:
            word.append(letter)
        guessed = ["*"]*len(word)    
        already_guessed = []
        continue
#if the word isn't guessed correctly 
    if guess_left == 0:
      print("\n The correct word was: " + "".join(word))
      restart = get_option()
      if restart == False:
        print("Thank you for playing!")
        break
      if restart == True:
        guess_left = 5
        playword = get_category()
        word = []
        for letter in playword:
            word.append(letter)
        guessed = ["*"]*len(word)
        already_guessed = []
        continue
  
  
  

  
  
  
  

        