import datetime


def get_date_info(time_point: str):
    """
    Get date information for enrolled subject from user(i.e. follow up time)
    :param time_point: time point requested for user(i.e. enrollment vs follow up)
    :return: Screening date as datetime object
    """
    while True:
        try:
            value_from_user = input("What is the {} date MM/DD/YYYY [Leave Blank for Today] ".format(time_point))
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
        except ValueError:
            print("Please enter a date in the format MM/DD/YYYY")
            continue
    return value_from_user


def get_time_info(time_point: str):
    """
    Get time information for enrolled subject from user(i.e. enrollment)
    :param time_point: time point requested from user(enrollment vs follow up)
    :return: time point as datetime object
    """
    while True:
        try:
            value_from_user = input("What is the {} time MM:HH [Leave Blank for Today] ".format(time_point))
            # TODO: add validation for correct time input
            if value_from_user and value_from_user != " ":  # Need better validation
                hour, minute = value_from_user.split(":")
                value_from_user = datetime.time(int(hour), int(minute))
                return value_from_user
            if not value_from_user:
                value_from_user = datetime.datetime.time(datetime.datetime.now())
                return value_from_user
            if not value_from_user.strip():  # Bad entry
                print("Please enter a time or leave blank for now")
                continue
        except ValueError:
            print("Please enter a time in the format HH:MM")
            continue


def get_info_from_user(requested_info: str):
    """
    Get requested info for enrolled patient from user(i.e. subject_initials)
    :param requested_info: name of variable requested as str
    :return: value given by user as str
    """
    while True:
        value_from_user = input("What is the {} for subject ".format(requested_info))
        # TODO: add validation for correct type input
        value_from_user = value_from_user.strip()
        if value_from_user:
            return value_from_user
        if not value_from_user:  # Bad entry
            print("Please enter a valid {} for subject")
