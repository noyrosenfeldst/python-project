import os


def GetSumSize(file_list):
    """Return the total size of all files."""

    total_size = 0

    for file_path in file_list:
        try:
            with open(file_path, "r"):
                file_size = os.path.getsize(file_path)

                total_size += file_size

        except FileNotFoundError:
            print(f"{file_path} was not found.")

        except PermissionError:
            print(f"No permission to access {file_path}.")

    print(f"Total size: {total_size} bytes")

    return total_size


# check
GetSumSize(["question1.py", "question2.py"])