from datetime import time
from itertools import islice

import openpyxl
import pandas as pd


def print_stats(stat_type: str, patient_dict: dict):
    """
    Helper function for printing the stats from the patient data in a nice format
    :param stat_type: Stat type to print (Age, Race, Etc)
    :param patient_dict: dictionary containing stat data
    :return: No return
    """
    print("{} stats".format(stat_type), end="\n---------------------------\n")
    for stat, value in patient_dict.items():
        print(stat, value, sep=":")
    print()


def get_basic_stats_by_date(log_path, log_sheet, log_type, start_date, end_date):
    """
    Get basic statistics for a log filtered by date
    :param log_path: pathway to log to create stats from  (i.e. Screening, Enrollment)
    :param log_sheet: name of the sheet in the log that contains data (i.e. Screening_Loo, Enrollment_Log)
    :param log_type: type of log (i.e. Screening, Enrollment)
    :param start_date: initial date
    :param end_date: end date
    :return: data frame filtered on start_date and end_date
    """
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = create_dataframe_from_log(log_path, log_sheet, log_type)
    df = df.loc[(df['{}Date'.format(log_type)] >= start_date) \
                & (df['{}Date'.format(log_type)] <= end_date)]
    get_stats(data_frame=df)
    return df


def get_stats(log_path=None, log_sheet=None, log_type=None, data_frame=None):
    """
    Gets basic statistics for a log or a filtered DataFram if given
    :param log_path: pathway to log to create stats from  (i.e. Screening, Enrollment)
    :param log_sheet: name of the sheet in the log that contains data (i.e. Screening_Loo, Enrollment_Log)
    :param log_type: type of log (i.e. Screening, Enrollment)
    :param data_frame: pre-filtered DataFrame generate stats for
    :return: No return
    """
    if log_path is not None and log_sheet is not None:
        df = create_dataframe_from_log(log_path, log_sheet, log_type)
    else:
        df = data_frame
    # Total subjects
    total_subjects_in_log = len(df)
    print("You have screened {} patients in total ".format(total_subjects_in_log))
    # Total by Sex
    if df.get('Sex') is not None:
        sex = (df['Sex'].value_counts())
        print_stats('Sex', sex.to_dict())
    # Total by Age
    if df.get('Age') is not None:
        age_stats = df['Age'].describe().to_dict()
        print_stats('Age', age_stats)
    # Total Eligible
    if df.get('Eligible') is not None:
        eligible = df['Eligible'].value_counts()
        print_stats('Eligibility', eligible.to_dict())
    # Reasons Ineligible
    if df.get('Reason_Ineligible') is not None:
        reason_ineligible = df['Reason_Ineligible'].value_counts()
        print_stats('Reason Ineligible', (reason_ineligible.to_dict()))
    # Enrolled
    if df.get('Enrolled') is not None:
        enrollment = df['Enrolled'].value_counts()
        print_stats('Enrollment', enrollment.to_dict())
    # Reason Not Enrolled
    if df.get('Reason_Not_Enrolled') is not None:
        reason_not_enrolled = df['Reason_Not_Enrolled'].value_counts()
        print_stats('Reason Not Enrolled', reason_not_enrolled.to_dict())
    return None


def create_dataframe_from_log(log_path, log_sheet, log_type):
    """
    Create  a DataFrame from a given log
    :param log_path: pathway to log to create stats from  (i.e. Screening, Enrollment)
    :param log_sheet: name of the sheet in the log that contains data (i.e. Screening_Loo, Enrollment_Log)
    :param log_type: type of log (i.e. Screening, Enrollment)
    :return:
    """
    work_book = openpyxl.load_workbook(log_path)
    work_sheet = work_book[log_sheet]
    data = work_sheet.values
    col_names = next(data)  # Get Headers as column name
    log_data = list(data)
    row_ids = [i for i, _ in enumerate(log_data)]  # Get count of subjects in file as row_id
    log_data = (islice(row, 0, None) for row in log_data)
    df = pd.DataFrame(log_data, index=row_ids, columns=col_names)
    # Convert Date Columns
    df['{}Date'.format(log_type)] = df['{}Date'.format(log_type)].apply(pd.to_datetime)
    # Convert Time Columns
    df['{}Time'.format(log_type)] = df['{}Time'.format(log_type)].apply(lambda x: time(*[int(item)
                                                                                         for item in x.split(":")
                                                                                         ])
                                                                        )
    # Convert Age to int
    df['Age'] = df['Age'].apply(pd.to_numeric)
    return df


def get_stats_by_time(log, log_sheet):
    return None
