from collections import namedtuple
import data_request_functions
import add_patient_to_excel_file

ScreenedPatient = namedtuple("Screened_Patient", ",".join(['Screening_Date', 'Screening_Time Subject_Initials',
                                                           'Medical_Record_Number', 'Age', 'Sex', 'Eligible',
                                                           'Reason_Ineligible', 'Enrolled',
                                                           'Reason_Not_Enrolled', 'Research_Assistant_Initials'
                                                           ]))
EnrolledPatient = namedtuple("Enrolled_Patient",
                             ",".join(['Subject_ID', 'Enrollment_Date', 'Enrollment_Time','Age', 'Sex',
                                       'Enrollment_Arm', 'Research_Assistant_Initials'
                                       ]))
LinkedPatient = namedtuple("Linked_Patient", ",".join(['Subject_ID', 'Medical_Record_Number','Enrollment_Date',
                                                       'Enrollment_Time', 'Subject_Name', 'Age', 'Sex',
                                                       'Research_Assistant_Initials'
                                                       ]))
FollowUpPatient = namedtuple("Follow_Up_Patient", ",".join(['Subject_ID', 'Enrollment_Date', 'Enrollment_Time',
                                                            'Follow_Up_Date', 'Follow_Up_Time', 'Follow_Up_Complete',
                                                            'Notes'
                                                            ]))


def get_screened_patient_data():
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


def get_enrolled_patient_data():
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


def get_master_linking_log_data():
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


def get_follow_up_data():
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
    patient = get_screened_patient_data()
    patient_data = patient._asdict()
    add_patient_to_excel_file.add_patient('Screening_Log.xlsx', patient_data, 'Screening_Log')
    patient = get_enrolled_patient_data()
    patient_data = patient._asdict()
    add_patient_to_excel_file.add_patient('Enrollment_Log.xlsx', patient_data, 'Enrollment_Log')
    patient = get_master_linking_log_data()
    patient_data = patient._asdict()
    add_patient_to_excel_file.add_patient('Master_Linking_Log.xlsx', patient_data, 'Master_Linking_Log')
    patient = get_follow_up_data()
    patient_data = patient._asdict()
    add_patient_to_excel_file.add_patient('Follow_Up_Log.xlsx', patient_data, 'Follow_Up_Log')

if __name__ == '__main__':
    main()
