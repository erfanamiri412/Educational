import os
def delete_file(file1):
    if os.path.exists(file1):
        os.remove(file1)
    else:
        print('file not found!')

delete_file('filing.txt')