from collections import namedtuple
import data_request_functions

FollowUpPatient = namedtuple("Follow_Up_Patient", ",".join(['enrollment_date', 'enrollment_time', 'subject_id',
                                                   'follow_up_date', 'follow_up_time'
                                                   ]))


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

