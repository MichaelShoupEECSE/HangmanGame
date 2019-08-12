import random
    
DICTIONARY_LIST = ['cat', 'page', 'mcafee', 'solidcore', 'table',
              'chair', 'lunch', 'robot', 'hotel', 'ford',
              'computer', 'dog', 'wannacry', 'glasses',
              'mouse', 'screen', 'book', 'woman', 'pie',
              'remote', 'some', 'other', 'virus', 'scan',
              'plane','found','answer','school','grow',
              'study','still','learn','plant','cover',
              'sun','four','between','state','keep',
              'eye','never','last','let','thought','city',
              'tree','cross','farm','hard','start','might',
              'story','saw','far','sea','draw','left',
              'run','press','close','night','real','life',
              'few','north','white','children','begin','got',
              'walk','example','ease','paper','group',
              'always','music','those','both','mark',
              'often','letter','until','mile','river','car',
              'mountain','stop','once','base','hear',
              'horse','cut','sure','watch','color','face',
              'wood','main','enough','plain','girl','usual',
              'young','ready','above','ever','red','though',
              'feel','talk','bird','soon','body','dog',
              'family','direct','pose','leave','song',
              'measure','door','product','black','short',
              'numeral','question','happen','complete',
              'ship','area','half','rock','order','fire',
              'south','problem','piece','told','knew',
              'since','top','whole','king','space','heard',
              'best','hour','better','true','during',
              'hundred','five','remember','step','early',
              'hold','west','ground','interest','reach',
              'fast','verb','sing','listen','six','table',
              'travel','less','morning','ten','simple',
              'several','vowel','toward','war','lay',
              'against','pattern','slow','center','love',
              'person','money','serve','appear','road','rain',
              'rule','govern','pull','cold','notice','voice',
              'unit','power','town','fine','certain','fly',
              'fall','lead','cry','dark','machine','note',
              'wait','plan','figure','star','box','noun',
              'field','rest','correct','able','pound',
              'done','beauty','drive','stood','contain','front',
              'teach','week','final','gave','green']

def hangman(word,games_won,games_lost):
    """
    Takes in the word to guess and the
    number of wins and losses this game.
    :param word:  string from dictionary
    :param games_won:  int
    :param games_lost: int
    """
    wrong = 0
    stages = ["",
              "_______       ",
              "|      |      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             ",
              "|___          "
              ]
    #list used for comparison
    rletters = list(word)
    
    #Shows how many characters there are
    #As well as the letters guessed right
    board = ["__" for i in word]
    
    #Creats a list of letters guessed to display
    guessed = []
    
    print(" Welcome to Hangman!",'\n',
          "Keep guessing until you get",'\n',
          "the word right or you lose.")
    print(board)

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg)
        guessed.append(char)
        win = False
        if char in rletters:
            for i in range(0,len(word)-1):
                if char in rletters:
                    cind = rletters.index(char)
                    board[cind] = char
                    rletters[cind] = '$'
        else:
            wrong += 1
        print("Letters guessed: {}".format(guessed))
        print((" ".join(board)))
        end_of_display = wrong + 1
        print("\n".join(stages[0: end_of_display]))
        if "__" not in board:
            #If there are no more blanks,
            #the game is won
            print("You win!")
            print("".join(board))
            win = True
            return win
    if not win:
        print("\n")
        print("You lose! The word was {}.".format(word))
        return win
    
def main():
    """
    Main function of the program. Calls
    the hangman function.
    """
    games_won = 0
    games_lost = 0
    while True:
        integ = random.randint(0,len(DICTIONARY_LIST)-1)
        play = input("Do you want to play? 'y' for yes. ")
        play = play.lower()
        if play == "y":
            win = hangman(DICTIONARY_LIST[integ],games_won, games_lost)
            #Removes the word from the list so it isn't played again
            DICTIONARY_LIST.pop(integ)
            if win:
                games_won += 1
            else:
                games_lost += 1
            print("Wins: {} Loses: {}".format(games_won, games_lost))
        else:
            break
if __name__ == '__main__':
    main()
