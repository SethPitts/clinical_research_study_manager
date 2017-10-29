import os
import sys


def make_directory(directory_path):
    try:
        if not os.path.isdir(directory_path):
            os.mkdir(directory_path)
        else:
            print("Directory already exist")
    except PermissionError as e:
        print(e)
        sys.exit(1)
