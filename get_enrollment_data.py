from collections import namedtuple
import data_request_functions


EnrolledPatient = namedtuple("Enrolled_Patient", ",".join(['enrollment_date', 'enrollment_time', 'subject_id', 'age', 'sex',
                                                  'enrollment_arm', 'research_assistant_initials'
                                                  ]))


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
    patient_data['research_assistant_initials'] = data_request_functions.get_info_from_user('research assistant initials')

    return EnrolledPatient(**patient_data)