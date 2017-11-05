import argparse
import os
import sys

from research_study_manager import create_directories, create_excel_files, load_project

parser = argparse.ArgumentParser(prog='Research Study Manager',
                                 description='Command line interface to manage some common research tasks')
parser.add_argument('-create_project', help='Creates a new project Projects Directory with the given name')
parser.add_argument('-load_project', help='Loads Project that you wish to manage')


def main():
    print(__file__)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    args = parser.parse_args(sys.argv[1:])
    if args.create_project is not None and args.create_project.strip():
        project_name = args.create_project.strip()
        project_path = os.path.join(BASE_DIR, 'Projects', project_name)
        print("Creating new project titled {}".format(project_name))
        create_directories.create_project_directories(project_path, project_name)
        print("Created log files for project {}".format(project_name))
        create_excel_files.create_project_excel_files(project_name, project_path)

    # Bad entry
    elif args.create_project is not None and not args.create_project.strip():
        print("You must supply a non empty string")
        sys.exit(1)

    if args.load_project is not None and args.load_project.strip():
        project_name = args.load_project.strip()
        load_project.load_project(BASE_DIR, project_name)
    # Bad Entry
    elif args.load_project is not None and not args.load_project.strip():
        print("You must supply a non empty string")


if __name__ == '__main__':
    main()
