def main():
    user_input = input("Input: ")
    word_without_vowels = shorten(user_input)
    print(f"Output: {word_without_vowels}")

def shorten(word):
    word_without_vowels = ""
    for letter in word:
        if not letter.lower() in ["a","e","i","o","u"]:
           word_without_vowels += letter
    return word_without_vowels

if __name__ == "__main__":
    main()