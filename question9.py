def AddWordIfNotExist(file_path, new_word):
    """Add a word to the file if it does not already exist."""

    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            words = file_content.split()

        if new_word not in words:
            with open(file_path, "a") as file:
                file.write(" " + new_word)
            print(f'"{new_word}" was added to the file.')

        else:
            print(f'"{new_word}" already exists in the file.')

    except FileNotFoundError:
        print("File was not found.")

    except PermissionError:
        print("No permission to access the file.")


# check
AddWordIfNotExist("example.txt", "hello")