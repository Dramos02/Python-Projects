def reverse_Capitalized(word):
    word = word.strip()
    reverse_Word = word[::-1]
    print(f"String: {word}")
    print(f"Reversed: {reverse_Word.upper()} ({len(reverse_Word)} characters)")
    """
    In line 2 I used .strip() to remove spaces from begin - end so the count characters stay
    In line 3 I initialize the length of the word with :: that will start from beginning to end then -1 to reverse it
    In line 5 I used .upper() to Capitalized the word and len to get the element count of the word
    """


while True:
    word = input("Enter a word: ")
    if all(x.isalpha() or x.isspace()
           for x in word):
        reverse_Capitalized(word)
        break
    print("Invalid input. Please enter a Word with only LETTERS.")

    """
    In line 14 i used .isalpha() to return True if the string only contains a-z or A-Z then
    i used isspace() to return True if there is space within/between a word
    Then call the reverse_Capitalized to prints out the needed information 
    such us the word to reversed and the Reversed and Capitalized word
     Copyrights © https://github.com/Dramos02
    """