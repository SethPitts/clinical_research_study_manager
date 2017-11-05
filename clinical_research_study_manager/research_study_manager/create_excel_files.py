from collections import OrderedDict

import openpyxl
import os


def get_screening_headers() -> list:
    screening_headers = OrderedDict()
    screening_headers['ScreeningDate'] = 'date'
    screening_headers['ScreeningTime'] = 'time'
    screening_headers['SubjectInitials'] = 'initials'
    screening_headers['MedicalRecordNumber'] = 'mrn'
    screening_headers['Age'] = 'age'
    screening_headers['Sex'] = 'sex'
    screening_headers['Eligible'] = 'yes_no_unknown'
    screening_headers['ReasonIneligible'] = 'reasons_not_eligible'
    screening_headers['Enrolled'] = 'yes_no_na'
    screening_headers['ReasonNotEnrolled'] = 'reasons_not_enrolled'
    screening_headers['ResearchAssistantInitials'] = 'initials'
    return list(screening_headers.keys())


def get_enrollment_headers() -> list:
    enrollment_headers = OrderedDict()
    enrollment_headers['SubjectID'] = 'subject_id'
    enrollment_headers['EnrollmentDate'] = 'date'
    enrollment_headers['EnrollmentTime'] = 'time'
    enrollment_headers['Age'] = 'age'
    enrollment_headers['Sex'] = 'sex'
    enrollment_headers['EnrollmentArm'] = 'enrollment_arm'
    enrollment_headers['ResearchAssistantInitials'] = 'initials'
    return list(enrollment_headers.keys())


def get_follow_up_headers() -> list:
    follow_up_headers = OrderedDict()
    follow_up_headers['SubjectID'] = 'subject_id'
    follow_up_headers['EnrollmentDate'] = 'date'
    follow_up_headers['EnrollmentTime'] = 'time'
    follow_up_headers['FollowUpDate'] = 'date'
    follow_up_headers['FollowUpTime'] = 'time'
    follow_up_headers['FollowUpComplete'] = 'yes_no_na'
    follow_up_headers['Notes'] = 'yes_no_na'
    return list(follow_up_headers.keys())


def get_linking_log_headers() -> list:
    linking_headers = OrderedDict()
    linking_headers['SubjectID'] = 'subject_id'
    linking_headers['MedicalRecordNumber'] = 'mrn'
    linking_headers['EnrollmentDate'] = 'date'
    linking_headers['EnrollmentTime'] = 'time'
    linking_headers['SubjectName'] = 'name'
    linking_headers['Age'] = 'age'
    linking_headers['Sex'] = 'sex'
    linking_headers['ResearchAssistantInitials'] = 'initials'
    return list(linking_headers.keys())


def create_excel_file(project_name: str, project_path: str, file_name: str, headers: list):
    if file_name != 'Master_Linking_Log.xlsx':
        excel_file_path = os.path.join(project_path, 'logs', file_name)
    else:
        excel_file_path = os.path.join(project_path, 'logs', 'logs_with_phi', file_name)

    new_work_book = openpyxl.Workbook()
    work_sheet = new_work_book.active
    work_sheet.title = file_name.replace('.xlsx', '')
    work_sheet.append(headers)
    new_work_book.save(os.path.join(excel_file_path))
    print("Created {} log for {} at {}".format(file_name, project_name, excel_file_path))


def create_project_excel_files(project_name: str, project_path: str):
    file_names_and_headers = {'Screening_Log.xlsx': get_screening_headers(),
                              'Enrollment_Log.xlsx': get_enrollment_headers(),
                              'Follow_Up_Log.xlsx': get_follow_up_headers(),
                              'Master_Linking_Log.xlsx': get_linking_log_headers(),
                              }
    for file_name, headers in file_names_and_headers.items():
        create_excel_file(project_name, project_path, file_name, headers)
