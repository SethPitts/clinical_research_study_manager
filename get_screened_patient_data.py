import datetime
from collections import namedtuple

ScreenedPatient = namedtuple("Screened_Patient", "screening_date screening_time subject_initials "
                                                 "medical_record_number age sex eligibility_status "
                                                 "reason_ineligible enrollment_status reason_not_enrolled "
                                                 "research_assistant_initials")


def get_screened_patient_data():
    """
    Get screening data for a single screened subject
    :return: Named Tuple with subjects data
    """
    patient_data = dict()
    patient_data['screening_date'] = get_screening_date()
    patient_data['screening_time'] = get_screening_time()
    patient_data['subject_initials'] = get_info_from_user('subject initials')
    patient_data['medical_record_num'] = get_info_from_user('medical record number')
    patient_data['age'] = get_info_from_user('age')
    patient_data['sex'] = get_info_from_user('sex')
    patient_data['eligibility_status'] = get_info_from_user('eligibility status')
    patient_data['reason_ineligible'] = get_info_from_user('reason ineligible')
    patient_data['enrollment_status'] = get_info_from_user('enrollment status')
    patient_data['reason_not_enrolled'] = get_info_from_user('reason not enrolled')
    patient_data['research_assistant_initials'] = get_info_from_user('research assistant initials')

    return ScreenedPatient(**patient_data)


def get_screening_time():
    """
    Get screening time from user
    :return: screening time as datetime object
    """
    while True:
        screening_time = input("What is the time of screening MM:HH [Leave Blank for Today]")
        # TODO: add validation for correct time input
        if screening_time and screening_time != " ":  # Need better validation
            hour, minute = screening_time.split(":")
            screening_time = datetime.time(hour, minute)
            return screening_time
        if not screening_time:
            screening_time = datetime.datetime.time(datetime.datetime.now())
            return screening_time
        if not screening_time.strip():  # Bad entry
            print("Please enter a time or leave blank for now")
            continue


def get_screening_date():
    """
    Get screening date from user
    :return: Screening date as datetime object
    """
    while True:
        screening_date = input("What is the date screened MM/DD/YYYY [Leave Blank for Today]")
        # TODO: add validation for correct date input
        if screening_date and screening_date != ' ':  # Need better validation
            day, month, year = screening_date.split("/")
            screening_date = datetime.datetime(int(year), int(month), int(day))
            break
        if not screening_date:
            screening_date = datetime.date.today()
            break
        if not screening_date.strip():  # Bad entry
            print("Please enter a date or leave blank for Today")
    return screening_date


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
