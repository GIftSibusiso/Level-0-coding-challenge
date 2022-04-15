def vowels(word):
    VOWELS = "aeiou"
    present_vowels = ""

    for letter in word.lower():
        if letter in VOWELS and letter not in present_vowels:
            present_vowels += letter + ", "
    
    for i in range(2):
        present_vowels = present_vowels[:-1]

    return print(f"Vowels: {present_vowels}")
 