def word_count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found"

filename = input("Enter filename: ")
print(f"Word count: {word_count(filename)}")
