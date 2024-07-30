def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    text = input("Please enter a sentence or paragraph: ").strip()

    if not text:
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return
    word_count = count_words(text)
    print(f"The number of words in the entered text is: {word_count}")
if __name__ == "__main__":
    main()
