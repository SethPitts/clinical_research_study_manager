import datetime
from collections import namedtuple

LinkedPatient = namedtuple("Linked_Patient", "enrollment_date enrollment_time subject_id "
                                                 "medical_record_number age sex enrollment_arm "
                                                 "research_assistant_initials")


def get_master_linking_log_data():
    """
    Get master linking data for an enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['enrollment_date'] = get_enrollment_date()
    patient_data['enrollment_time'] = get_enrollment_time()
    patient_data['subject_id'] = get_info_from_user('subject id')
    patient_data['medical_record_number'] = get_info_from_user('medical_record_number')
    patient_data['age'] = get_info_from_user('age')
    patient_data['sex'] = get_info_from_user('sex')
    patient_data['enrollment_arm'] = get_info_from_user('enrollment arm')
    patient_data['research_assistant_initials'] = get_info_from_user('research assistant initials')

    return LinkedPatient(**patient_data)


def get_enrollment_time():
    """
    Get enrollment time from user
    :return: screening time as datetime object
    """
    while True:
        enrollment_time = input("What is the time of screening MM:HH [Leave Blank for Today]")
        # TODO: add validation for correct time input
        if enrollment_time and enrollment_time != " ":  # Need better validation
            hour, minute = enrollment_time.split(":")
            enrollment_time = datetime.time(hour, minute)
            return enrollment_time
        if not enrollment_time:
            enrollment_time = datetime.datetime.time(datetime.datetime.now())
            return enrollment_time
        if not enrollment_time.strip():  # Bad entry
            print("Please enter a time or leave blank for now")
            continue


def get_enrollment_date():
    """
    Get enrollment date from user
    :return: Screening date as datetime object
    """
    while True:
        enrollment_date = input("What is the date screened MM/DD/YYYY [Leave Blank for Today]")
        # TODO: add validation for correct date input
        if enrollment_date and enrollment_date != ' ':  # Need better validation
            day, month, year = enrollment_date.split("/")
            enrollment_date = datetime.datetime(int(year), int(month), int(day))
            break
        if not enrollment_date:
            enrollment_date = datetime.date.today()
            break
        if not enrollment_date.strip():  # Bad entry
            print("Please enter a date or leave blank for Today")
    return enrollment_date


def get_info_from_user(requested_info: str):
    """
    Get requested info for enrolled patient for linking log from user(i.e. subject_initials)
    :param requested_info: name of variable requested as str
    :return: value given by user as str
    """
    while True:
        value_from_user = input("What is the {} for screened subject".format(requested_info))
        # TODO: add validation for correct itype input
        value_from_user = value_from_user.strip()
        if value_from_user:
            return value_from_user
        if not value_from_user:  # Bad entry
            print("Please enter the screened subjects initials")
