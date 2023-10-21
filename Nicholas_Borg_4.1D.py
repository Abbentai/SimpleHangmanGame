from random import randint 

def displayTitle(titleFilePath):
    '''Opens the hangmanWord.txt file,reading each line and prints it '''
    try:
        fileopen = open(titleFilePath, "r") #opens the hangmanWord.txt file in read mode
        for line in (fileopen): #every line in the txt file is read and printed with any extra spaces being stripped
            print(line.rstrip())
        fileopen.close()
    except FileNotFoundError: 
        print("An error occurred while trying to access file... Exiting application")
        exit()
    except IOError:
        print("An error occurred while trying to access file... Exiting application")
        exit()

def generateRandomWord(wordsFilePath):
    '''Generates a random index and associates the index with a word from a predetermined list and assigns it to the word variable '''
    global word
    global backupWords
    try:
        fileopen = open(wordsFilePath, "r")#opens the hangmanWord.txt file in read mode
    except FileNotFoundError: #in the case that the ListOfWord.txt file is not able to be accessed, a backup list of words will be used instead
        print("Words file not found... backup words will be used instead")
        index = randint(1,6)
        word = backupWords[index]
        return word
    except IOError:
        print("An error occurred while trying to fetch the word... Exiting application")
        exit()
    else:
        cnt = 0
        line = randint(1,213) #generates random index
        while(cnt != line): #this loop continues to read each line until cnt is equal to the line index
            word = fileopen.readline(line)
            cnt += 1
            word = word.strip()
        return 

def loadHangmanDrawings(hangmanDrawingsFilePath):
    '''Reads the hangmanDrawings3.txt file while assigning the values in a list when two new lines are present in the file'''
    global hangmanDrawingsList
    try:
        fileopen = open(hangmanDrawingsFilePath, "r") #opens the hangmanWord.txt file in read mode
        hangmanDrawingsList = fileopen.read().split("\n\n") 
        fileopen.close

    except FileNotFoundError: 
        print("An error occurred while trying to access the hangman drawings file...Exiting application")
        exit()
    except IOError:
        print("An error occurred while trying to access the hangman drawings file...Exiting application")
        exit()

#Variables Used
title = "hangmanWord.txt"
hangmanDrawings = "hangmanDrawings3.txt"
wordList = "ListOfWords.txt"
backupWords = ["abruptly", "buffalo", "cricket", "duplex", "fashion", "galaxy"] #words used instead of ListOfWords.txt incase it can't be accessed
word = "" #word to guess
shownWord = [] #A list containing the word and letters that the user has guesses
currentWord = "" #A string with all of the letters that the user has guessed
guessedLetters = [] #letters already guessed by the user
chances = 6# number of user attempts
hangmanDrawingsList = [] #stores hangman drawings
drawingCount = 0 #drawing index
alphabet = [chr(x) for x in range (97,123,1)] #every character in the latin alphabet converted from its Decimal Unicode Form


#start of code
displayTitle(title) #prints title
loadHangmanDrawings(hangmanDrawings) #loads drawing
generateRandomWord(wordList) #generates word
word.strip()
for i in range (0,len(word)): #dashes shown to represent the word
    shownWord.append("_")

while True:
    print(hangmanDrawingsList[drawingCount]) #prints drawing
    print(*shownWord, sep=" ")
    print("{",(', ').join(guessedLetters),"}") #displays the letters guessed by the user
    if (chances == 0): #when user has no more attempts the loop is exited, ending the program
                    word = ('"' + word.strip() + '"')
                    print('You lost the game. The correct word was', word)
                    break
    elif (currentWord == word):
        print("Well done... You guessed the word")
        break
    userInput = input("Guess a letter: ")
    userInput = userInput.lower() #makes any input from the user lowercase
    charIndex = 0 #Character Index
    
    for letterInput in (userInput): 
        if ((userInput.isalpha()) == True): #checks whether letterInput contains only letters
            if ((letterInput in word) == True):
                for i in range (-1,len(alphabet)):
                            if (letterInput == alphabet[i]): #continues to check whether every element in the alphabet list is equal to letterInput
                                guessedLetters.append(alphabet.pop(i)) #letter is moved from the alphabet list to the guessedLetters list    
                                break
                            while (charIndex < len(word)): 
                                if (letterInput == word[charIndex]): #checks if the letter is equal to each letter 
                                    shownWord.pop(charIndex) #removes the blank character from the shownWordList
                                    shownWord.insert(charIndex,letterInput) #replaces the previously removed character with the letter inputted by the user
                                    currentWord = ''.join([str(elem) for elem in shownWord]) #converts and concatenated every element in the shownWord list into a string
                                charIndex += 1
                            charIndex = 0
            else:
                for i in range (0,len(alphabet)):
                    if ((letterInput in alphabet[i]) == True):

                        guessedLetters.append(alphabet.pop(i))
                        chances -= 1
                        drawingCount += 1
                        break
        else:
            while ((userInput.isalpha()) == False): 
                userInput = input("Please enter only letters of the alphabet: ") #continuously prompts the user to input a letter until is inputted
