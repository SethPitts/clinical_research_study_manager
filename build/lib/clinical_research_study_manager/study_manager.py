import argparse
import os
import sys

from clinical_research_study_manager import create_directories, create_excel_files, load_project

parser = argparse.ArgumentParser(prog='Research Study Manager',
                                 description='Command line interface to manage some common research tasks')
parser.add_argument('-create_project', metavar='Project_Name',
                    help='Creates a new project titled Project_Name in the Projects directory')
parser.add_argument('-load_project', metavar='Project_Name',
                    help='Loads Project Project_Name from the Projects directory for study activities')
parser.add_argument('-list_projects', action='store_true', help='List available projects to load')


def main():
    start()


def start():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Create project directory if needed
    project_directory = os.path.join(BASE_DIR, 'Projects')
    if not os.path.exists(project_directory):
        os.mkdir(project_directory)
    args = parser.parse_args()
    # Create new project
    if args.create_project is not None and args.create_project.strip():
        project_name = args.create_project.strip()
        project_path = os.path.join(project_directory, project_name)
        print("Creating new project titled {}".format(project_name))
        create_directories.create_project_directories(project_path, project_name)
        print("Created log files for project {}".format(project_name))
        create_excel_files.create_project_excel_files(project_path, project_name)
    # Bad entry
    elif args.create_project is not None and not args.create_project.strip():
        print("You must supply a non empty string")
        sys.exit(1)
    # load specific project
    if args.load_project is not None and args.load_project.strip():
        project_name = args.load_project.strip()
        project_path = os.path.join(project_directory, project_name)
        if os.path.exists(project_path) and os.path.isdir(project_path):
            load_project.load_project(project_path, project_name)
        else:
            print('Project does not exist')
            sys.exit(1)
    # Bad Entry
    elif args.load_project is not None and not args.load_project.strip():
        print("You must supply a non empty string")

    # Load list of projects for user to choose from
    if args.list_projects is True:
        print(os.listdir(project_directory))
        current_projects = {pid + 1: project
                            for pid, project in enumerate(os.listdir(project_directory))
                            if os.path.isdir(os.path.join(project_directory, project))
                            }
        print(current_projects)
        # Create dict of projects to
        if current_projects:
            while True:
                print('Current Projects are: ')
                for pid, project_title in current_projects.items():
                    print('{} : {}'.format(pid, project_title))

                choice = (input('Please choose a project, q to quit. '))
                choice = int(choice) if choice.isnumeric() else choice
                if current_projects.get(choice):
                    project_title = current_projects[choice]
                    project_path = os.path.join(project_directory, project_title)
                    load_project.load_project(project_path, project_title)
                    sys.exit(0)
                elif choice.lower() == 'q':
                    sys.exit(0)
                else:
                    print('Please enter a valid choice')
                    continue


if __name__ == '__main__':
    main()
