from collections import namedtuple
import data_request_functions

ScreenedPatient = namedtuple("Screened_Patient", ",".join(['screening_date', 'screening_time subject_initials',
                                                           'medical_record_number', 'age', 'sex', 'eligibility_status',
                                                           'reason_ineligible', 'enrollment_status',
                                                           'reason_not_enrolled', 'research_assistant_initials'
                                                           ]))

LinkedPatient = namedtuple("Linked_Patient", ",".join(['enrollment_date', 'enrollment_time', 'subject_id',
                                                       'medical_record_number', 'age', 'sex', 'enrollment_arm',
                                                       'research_assistant_initials'
                                                       ]))

FollowUpPatient = namedtuple("Follow_Up_Patient", ",".join(['enrollment_date', 'enrollment_time', 'subject_id',
                                                            'follow_up_date', 'follow_up_time'
                                                            ]))

EnrolledPatient = namedtuple("Enrolled_Patient",
                             ",".join(['enrollment_date', 'enrollment_time', 'subject_id', 'age', 'sex',
                                       'enrollment_arm', 'research_assistant_initials'
                                       ]))


def get_screened_patient_data():
    """
    Get screening data for a single screened subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['screening_date'] = data_request_functions.get_date_info('screening')
    patient_data['screening_time'] = data_request_functions.get_time_info('screening')
    patient_data['subject_initials'] = data_request_functions.get_info_from_user('subject initials')
    patient_data['medical_record_number'] = data_request_functions.get_info_from_user('medical record number')
    patient_data['age'] = data_request_functions.get_info_from_user('age')
    patient_data['sex'] = data_request_functions.get_info_from_user('sex')
    patient_data['eligibility_status'] = data_request_functions.get_info_from_user('eligibility status')
    patient_data['reason_ineligible'] = data_request_functions.get_info_from_user('reason ineligible')
    patient_data['enrollment_status'] = data_request_functions.get_info_from_user('enrollment status')
    patient_data['reason_not_enrolled'] = data_request_functions.get_info_from_user('reason not enrolled')
    patient_data['research_assistant_initials'] = data_request_functions.get_info_from_user(
        'research assistant initials')

    return ScreenedPatient(**patient_data)


def get_master_linking_log_data():
    """
    Get master linking data for an enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['enrollment_date'] = data_request_functions.get_date_info('enrollment')
    patient_data['enrollment_time'] = data_request_functions.get_time_info('enrollment')
    patient_data['subject_id'] = data_request_functions.get_info_from_user('subject id')
    patient_data['medical_record_number'] = data_request_functions.get_info_from_user('medical_record_number')
    patient_data['age'] = data_request_functions.get_info_from_user('age')
    patient_data['sex'] = data_request_functions.get_info_from_user('sex')
    patient_data['enrollment_arm'] = data_request_functions.get_info_from_user('enrollment arm')
    patient_data['research_assistant_initials'] = data_request_functions.get_info_from_user(
        'research assistant initials')

    return LinkedPatient(**patient_data)


def get_follow_up_data():
    """
    Get follow up data for a single enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['enrollment_date'] = data_request_functions.get_date_info('enrollment')
    patient_data['enrollment_time'] = data_request_functions.get_time_info('enrollment')
    patient_data['follow_up_date'] = data_request_functions.get_info_from_user('follow_up')
    patient_data['follow_up_time'] = data_request_functions.get_info_from_user('follow_up')
    patient_data['subject_id'] = data_request_functions.get_info_from_user('subject id')

    return FollowUpPatient(**patient_data)


def get_enrolled_patient_data():
    """
    Get enrollment data for an enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['enrollment_date'] = data_request_functions.get_date_info('enrollment')
    patient_data['enrollment_time'] = data_request_functions.get_time_info('enrollment')
    patient_data['subject_id'] = data_request_functions.get_info_from_user('subject id')
    patient_data['age'] = data_request_functions.get_info_from_user('age')
    patient_data['sex'] = data_request_functions.get_info_from_user('sex')
    patient_data['enrollment_arm'] = data_request_functions.get_info_from_user('enrollment arm')
    patient_data['research_assistant_initials'] = data_request_functions.get_info_from_user(
        'research assistant initials')

    return EnrolledPatient(**patient_data)


def main():
    patient = get_screened_patient_data()
    print(patient)
    patient = get_enrolled_patient_data()
    print(patient)
    patient = get_master_linking_log_data()
    print(patient)
    patient = get_follow_up_data()
    print(patient)


if __name__ == '__main__':
    main()
