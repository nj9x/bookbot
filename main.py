def word_counter(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
    word_counter(file_contents)
    print(word_counter(file_contents))

if __name__ == "__main__":
    main()