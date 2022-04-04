# Word
word = list("audio")

# Check if answered
answered = False
guesses = 0
answer = []

# Loop until answered
while not answered and guesses < 5:

    # User input
    guess = list(input("Word: "))

    # Check each letter
    for i in range(5):

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
    if "".join(answer) == "ggggg":
        answered = True
    else:
        guesses += 1
        answer = []

# Correct answer?
if answered:
    print("Correct! The word was", "".join(word), "and you did it in", guesses + 1, "tries!")
else:
    print("You lose! The correct word is", "".join(word))