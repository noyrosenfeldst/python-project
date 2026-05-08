import os


def GetFileSize(file_name):
    """Return the size of a file in bytes."""
    try:
        with open(file_name, "r"):
            file_size = os.path.getsize(file_name)
            print(f"The size of {file_name} is: {file_size} bytes")
            return file_size

    except FileNotFoundError:
        print("File was not found.")

    except PermissionError:
        print("No permission to access the file.")

    return -1

# check
size = GetFileSize("question1.py")
