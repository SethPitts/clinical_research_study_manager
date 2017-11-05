import os
import sys
import research_study_manager as rsm


def manage_project(project_name: str, project_path: str):

    while True:
        # Ask for what the user would like to do
        print("1. Enter Patients on Screening Log")
        print("2. Enter Patients on Enrollment Log")
        print("3. Enter Patients on Follow Up Log")
        print("4. Enter Patients on Master Linking Log")
        choice = input("What actions would you like to take, q to quit ")

        choices = {'1': rsm.enter_patient_on_log.enter_screened_patient,
                   '2': rsm.enter_patient_on_log.enter_enrolled_patient,
                   '3': rsm.enter_patient_on_log.enter_follow_up_patient,
                   '4': rsm.enter_patient_on_log.enter_linking_log_patient,
                   }

        if choice is not None and choice.strip() and choices.get(choice) is not None:
            choices[choice](project_name, project_path)

        elif choice is not None and choice.strip() and choice.lower() == 'q':
            break
        # Bad Entry
        else:
            print("Please enter a valid choice")