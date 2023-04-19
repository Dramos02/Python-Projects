#Initialize array for the word_bank
word_Bank = []

#This loop will initialize the program
while True:
    word = str(input("Enter a word: "))
    #this will validate the empty user's input
    while not word:
        print("Please dont leave it blank/empty.")
        word = input("Enter a word: ")
    word_Bank.append(word)

    choices = input("Do you want to try again? [Y/N] ")
    while choices not in ["Y", "y", "N", "n"]:  #This is validates the choices needed only for user's input
        print("Invalid choice. Please enter Y or N.")
        choices = input("Do you want to try again? [Y/N] ")
    if choices in ["N", "n"]:
        break

print("You entered", len(word_Bank), 'word/s')
print("Words you entered: ")
for x in word_Bank:
    print("", x)





"""
copyright @ https://github.com/Dramos02
"""