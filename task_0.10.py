def common_characters(word1, word2):
    shared_letters = ""
    word1 = word1.lower()
    word2 = word2.lower()

    for letter in word1:
        if letter in word2 and letter not in shared_letters:
            shared_letters += letter + ", "
    
    for i in range(2):
        shared_letters = shared_letters[:-1]

    print(f"Common letters: {shared_letters}")
