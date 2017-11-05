import os
import sys
from research_study_manager.manage_project import manage_project


def load_project(BASE_DIR: str, project_name: str):
    project_path = os.path.join(BASE_DIR, project_name)
    if os.path.isdir(project_path):
        print("Opening {}".format(project_name))
        manage_project(project_name, project_path)

    else:
        print("{} does not exist")
        sys.exit(1)
