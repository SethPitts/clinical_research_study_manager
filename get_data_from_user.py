import os
from collections import namedtuple

import add_patient_to_excel_file
import data_request_functions

ScreenedPatient = namedtuple("Screened_Patient", ",".join(['Screening_Date', 'Screening_Time Subject_Initials',
                                                           'Medical_Record_Number', 'Age', 'Sex', 'Eligible',
                                                           'Reason_Ineligible', 'Enrolled',
                                                           'Reason_Not_Enrolled', 'Research_Assistant_Initials'
                                                           ]))
EnrolledPatient = namedtuple("Enrolled_Patient",
                             ",".join(['Subject_ID', 'Enrollment_Date', 'Enrollment_Time', 'Age', 'Sex',
                                       'Enrollment_Arm', 'Research_Assistant_Initials'
                                       ]))
LinkedPatient = namedtuple("Linked_Patient", ",".join(['Subject_ID', 'Medical_Record_Number', 'Enrollment_Date',
                                                       'Enrollment_Time', 'Subject_Name', 'Age', 'Sex',
                                                       'Research_Assistant_Initials'
                                                       ]))
FollowUpPatient = namedtuple("Follow_Up_Patient", ",".join(['Subject_ID', 'Enrollment_Date', 'Enrollment_Time',
                                                            'Follow_Up_Date', 'Follow_Up_Time', 'Follow_Up_Complete',
                                                            'Notes'
                                                            ]))


def to_dict(func: namedtuple):
    """Converts a named tuple to its order dictionary form"""

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)._asdict()

    return wrapper


@to_dict
def get_screened_patient_data() -> ScreenedPatient:
    """
    Get screening data for a single screened subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['Screening_Date'] = data_request_functions.get_date_info('screening')
    patient_data['Screening_Time'] = data_request_functions.get_time_info('screening')
    patient_data['Subject_Initials'] = data_request_functions.get_info_from_user('subject initials')
    patient_data['Medical_Record_Number'] = data_request_functions.get_info_from_user('medical record number')
    patient_data['Age'] = data_request_functions.get_info_from_user('age')
    patient_data['Sex'] = data_request_functions.get_info_from_user('sex')
    patient_data['Eligible'] = data_request_functions.get_info_from_user('eligibility status')
    patient_data['Reason_Ineligible'] = data_request_functions.get_info_from_user('reason ineligible')
    patient_data['Enrolled'] = data_request_functions.get_info_from_user('enrollment status')
    patient_data['Reason_Not_Enrolled'] = data_request_functions.get_info_from_user('reason not enrolled')
    patient_data['Research_Assistant_Initials'] = data_request_functions.get_info_from_user(
        'research assistant initials')

    return ScreenedPatient(**patient_data)


@to_dict
def get_enrolled_patient_data() -> EnrolledPatient:
    """
    Get enrollment data for an enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['Subject_ID'] = data_request_functions.get_info_from_user('subject id')
    patient_data['Enrollment_Date'] = data_request_functions.get_date_info('enrollment')
    patient_data['Enrollment_Time'] = data_request_functions.get_time_info('enrollment')
    patient_data['Age'] = data_request_functions.get_info_from_user('age')
    patient_data['Sex'] = data_request_functions.get_info_from_user('sex')
    patient_data['Enrollment_Arm'] = data_request_functions.get_info_from_user('enrollment arm')
    patient_data['Research_Assistant_Initials'] = data_request_functions.get_info_from_user(
        'research assistant initials')

    return EnrolledPatient(**patient_data)


@to_dict
def get_master_linking_log_data() -> LinkedPatient:
    """
    Get master linking data for an enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['Subject_ID'] = data_request_functions.get_info_from_user('subject_id')
    patient_data['Medical_Record_Number'] = data_request_functions.get_info_from_user('medical_record_number')
    patient_data['Enrollment_Date'] = data_request_functions.get_date_info('enrollment')
    patient_data['Enrollment_Time'] = data_request_functions.get_time_info('enrollment')
    patient_data['Subject_Name'] = data_request_functions.get_info_from_user('subject_name')
    patient_data['Age'] = data_request_functions.get_info_from_user('age')
    patient_data['Sex'] = data_request_functions.get_info_from_user('sex')
    patient_data['Research_Assistant_Initials'] = data_request_functions.get_info_from_user(
        'research assistant initials')

    return LinkedPatient(**patient_data)


@to_dict
def get_follow_up_data() -> FollowUpPatient:
    """
    Get follow up data for a single enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['Subject_ID'] = data_request_functions.get_info_from_user('subject id')
    patient_data['Enrollment_Date'] = data_request_functions.get_date_info('enrollment')
    patient_data['Enrollment_Time'] = data_request_functions.get_time_info('enrollment')
    patient_data['Follow_Up_Date'] = data_request_functions.get_date_info('follow up')
    patient_data['Follow_Up_Time'] = data_request_functions.get_time_info('follow up')
    patient_data['Follow_Up_Complete'] = data_request_functions.get_info_from_user('follow up complete')
    patient_data['Notes'] = data_request_functions.get_info_from_user('notes')
    return FollowUpPatient(**patient_data)


def main():
    screened_patient_data = get_screened_patient_data()
    add_patient_to_excel_file.add_patient(os.path.join('logs', 'Screening_Log.xlsx'), screened_patient_data,
                                          'Screening_Log')
    # enrolled_patient_data = get_enrolled_patient_data()
    # add_patient_to_excel_file.add_patient(os.path.join('logs','Enrollment_Log.xlsx'), enrolled_patient_data, 'Enrollment_Log')
    # linked_patient_data = get_master_linking_log_data()
    # add_patient_to_excel_file.add_patient(os.path.join('logs','logs_with_phi', 'Master_Linking_Log.xlsx'), linked_patient_data, 'Master_Linking_Log')
    # follow_up_patient_data = get_follow_up_data()
    # add_patient_to_excel_file.add_patient(os.path.join('logs','Follow_Up_Log.xlsx'), follow_up_patient_data, 'Follow_Up_Log')


if __name__ == '__main__':
    main()
