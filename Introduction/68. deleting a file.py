import os

def delete_file(file1):
    try:
        os.remove(file1)
    except FileNotFoundError:
        print(FileNotFoundError)

delete_file('filing.txt')