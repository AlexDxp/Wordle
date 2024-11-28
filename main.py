import random
fp = open("Words","r")
bold_start = '\033[1m'
bold_end   = '\033[0m'
underline_start = '\x1B[4m'
underline_end = '\x1B[0m'
print(bold_start + "Bold means correct letter in the correct place", bold_end)
print(underline_start + "Underline means correct letter in the in correct place", underline_end)
print("Regular means incorrect letter in the incorrect place")
listofwords = fp.read().split()
randomchoice = random.choice(listofwords)
guesses = ["_","_","_","_","_"]
lives = 6
while True:
    guess = input(' '.join(guesses))
    word = list(randomchoice)
    g = list(guess)
    wrong = []
    print(word)
    if guess in listofwords:
        for j in range(5):
            for i in range(5):
                if word[i] == g[i]:
                    guesses[i] = (bold_start + g[i].upper() + bold_end)
                elif word[i] != g[i] and word[j] == g[i]:
                    guesses[i] = (underline_start + g[i].upper() + underline_end)
                else:
                    guesses[i] = g[i]

    elif guess not in listofwords:
        print("Not in word list, use another word")
        continue
    if guess == randomchoice:
        print(randomchoice)
        print("You win!!")
        print("You won with",lives,"remaining")
        break
    lives -= 1
    print("Your have",lives,"lives remaining")
    if lives == 0:
        print("You lose")
        print("The word was",randomchoice)
        break