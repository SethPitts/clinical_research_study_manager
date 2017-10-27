import datetime
from collections import namedtuple

FollowUpPatient = namedtuple("Follow_Up_Patient", "enrollment_date enrollment_time subject_id "
                                                 "follow_up_date, follow_up_time")


def get_follow_up_data():
    """
    Get follow up data for a single enrolled subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['enrollment_date'] = get_enrollment_date('enrollment')
    patient_data['enrollment_time'] = get_enrollment_time('enrollment')
    patient_data['follow_up_date'] = get_enrollment_date('follow_up')
    patient_data['follow_up_time'] = get_enrollment_time('follow_up')
    patient_data['subject_id'] = get_info_from_user('subject id')
    patient_data['medical_record_number'] = get_info_from_user('medical_record_number')

    return FollowUpPatient(**patient_data)


def get_enrollment_time(time_point: str):
    """
    Get time information for enrolled subject from user(i.e. enrollment)
    :param time_point: time point requested from user(enrollment vs follow up)
    :return: time point as datetime object
    """
    while True:
        value_from_user = input("What is the {} time MM:HH [Leave Blank for Today]".format(time_point))
        # TODO: add validation for correct time input
        if value_from_user and value_from_user != " ":  # Need better validation
            hour, minute = value_from_user.split(":")
            value_from_user = datetime.time(hour, minute)
            return value_from_user
        if not value_from_user:
            value_from_user = datetime.datetime.time(datetime.datetime.now())
            return value_from_user
        if not value_from_user.strip():  # Bad entry
            print("Please enter a time or leave blank for now")
            continue


def get_enrollment_date(time_point: str):
    """
    Get date information for enrolled subject from user(i.e. follow up time)
    :param time_point: time point requested for user(i.e. enrollment vs follow up)
    :return: Screening date as datetime object
    """
    while True:
        value_from_user = input("What is the {} date MM/DD/YYYY [Leave Blank for Today]".format(time_point))
        # TODO: add validation for correct date input
        if value_from_user and value_from_user != ' ':  # Need better validation
            day, month, year = value_from_user.split("/")
            value_from_user = datetime.datetime(int(year), int(month), int(day))
            break
        if not value_from_user:
            value_from_user = datetime.date.today()
            break
        if not value_from_user.strip():  # Bad entry
            print("Please enter a date or leave blank for Today")
    return value_from_user


def get_info_from_user(requested_info: str):
    """
    Get requested info for screened patient from user(i.e. subject_initials)
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
