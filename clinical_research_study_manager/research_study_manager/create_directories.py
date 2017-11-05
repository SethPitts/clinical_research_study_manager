import os
import sys


def make_directory(project_path, directory_to_create, project_name):
    directory_path = os.path.join(project_path, directory_to_create)
    try:
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
            print("Created {} for project {} at {}".format(directory_to_create, project_name, project_path))
        else:
            if os.path.isdir(directory_path):
                print("Directory {} already exist".format(directory_path))
    except PermissionError as e:
        print(e)
        sys.exit(1)


def create_project_directories(project_path, project_name):
    # Create New Project Directory
    if not os.path.exists(project_path):
        os.mkdir(project_path)
    else:
        print("Proejct Directory already exit at {}".format(project_path))
    directories = ['patient_data[phi]', 'patient_data[de_identified]', 'logs', 'logs/logs_with_phi',
                   'data_visualization']
    for directory_to_create in directories:
        make_directory(project_path, directory_to_create, project_name)


def main():
    pass


if __name__ == '__main__':
    main()
