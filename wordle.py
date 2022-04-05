# Import random choice module
from random import choice

# Get all words
with open("words.txt", "r") as file:
    wordList = file.read().split()

# Word
word = list(choice(wordList))
wordLen = len(word)

# Tells the person length of word
print("The word is", wordLen, "letters long.\n")

# Check if answered
answered = False
inputted = False
guesses = 0
answer = []

# Loop until answered
while not answered and guesses < wordLen:

    # User input
    while not inputted:
        guess = list(input("Word: "))

        # Makes sure the guess is the correct length
        if len(guess) != wordLen:
            print("Incorrect guess, please try again. The length of the word is", wordLen)
        else:
            inputted = True

    # Check each letter
    for i in range(wordLen):

        # Is letter in word?
        if guess[i] in word:

            # Is letter in same place?
            if guess[i] == word[i]:
                answer.append("g")
            else:
                answer.append("o")
        
        # Letter not in word
        else:
            answer.append("n")

    # Prints final output
    print("".join(answer))

    # Is every letter in correct place?
    if "".join(answer) == "g" * wordLen:
        answered = True
    else:
        guesses += 1
        answer = []
        inputted = False

# Correct answer?
if answered:
    print("Correct! The word was", "".join(word), "and you did it in", guesses + 1, "tries!")
else:
    print("You lose! The correct word is", "".join(word))