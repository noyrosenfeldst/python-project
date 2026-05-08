def GetWordsFromFile(file_path):
    """Return all unique words from a file."""

    unique_words = set()

    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            words = file_content.split()
            for word in words:
                unique_words.add(word)

    except FileNotFoundError:
        print("File was not found.")

    except PermissionError:
        print("No permission to access the file.")

    return list(unique_words)


# check
print(GetWordsFromFile("question1.py"))