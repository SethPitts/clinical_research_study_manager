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


def main():
    make_directory('patient_data[phi]')
    make_directory('patient_data[de-identified]')
    make_directory('logs')
    make_directory('logs/logs_with_phi')
    make_directory('data_visualization')


if __name__ == '__main__':
    main()
