#This is the game of guessing word in which computer 
# will choose a word and user have to guess it and user
# will have only 6 life.
# ///////////////////
# Let's begin for the coding of this game without wasting any time////
import random
import Hangman_stages
import Wordfile
word_list=Wordfile.word #Here words are stored so that compiler can take it for further action.
choosen_word=random.choice(word_list)#Choosing random word from[word_list]
print(choosen_word)
lives=int(6)
display=[]#here the blank space for the [choosen word] form [word list] will be stored
for i in range(len(choosen_word)):#/choosen_word:/In this loop blank spaces are assigned equal to the [choosen_word] in display array/list.
    display+='_'
print(display) 
game_over=False 
while not game_over: 
    guessed_letter=input("Guess a letter:").lower()#Ask user to guess a letter
# //
    for position in range(len(choosen_word)):#This loop checks weather guessed letter is correct or not and replace the guessed letter with blank space
        letter=choosen_word[position]
        if letter ==guessed_letter:
         display[position]=guessed_letter
        else:
            pass
    print(f"{display}")
    if guessed_letter not in choosen_word:
       lives-=1
       if lives==0:
          print("OOP's You Loosed !")
          game_over=True
    if '_' not in display:
       game_over=True
       print(f"Congratulation You Won")      
    print(Hangman_stages.stages[lives])#Here we created a module named[Hangman_stages.py] in same file and from there we called [stages] library.
        
    
    

    