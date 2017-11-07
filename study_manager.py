import argparse
import os
import sys

from research_study_manager import create_directories, create_excel_files, load_project

parser = argparse.ArgumentParser(prog='Research Study Manager',
                                 description='Command line interface to manage some common research tasks')
parser.add_argument('-create_project', help='Creates a new project Projects Directory with the given name')
parser.add_argument('-load_project', help='Loads Project that you wish to manage')
parser.add_argument('-list_projects', default='Load Projects', help='List available projects to load')


def main():
    print(__file__)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.join(BASE_DIR, 'Projects')
    args = parser.parse_args(sys.argv[1:])
    # Create new project
    if args.create_project is not None and args.create_project.strip():
        project_name = args.create_project.strip()
        project_path = os.path.join(project_directory, project_name)
        print("Creating new project titled {}".format(project_name))
        create_directories.create_project_directories(project_path, project_name)
        print("Created log files for project {}".format(project_name))
        create_excel_files.create_project_excel_files(project_name, project_path)
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
    if args.list_projects is not None and args.list_projects.strip():
        print(os.listdir(project_directory))
        current_projects = {pid + 1: project
                            for pid, project in enumerate(os.listdir(project_directory))
                            if os.path.isdir(project)
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
