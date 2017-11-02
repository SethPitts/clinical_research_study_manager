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
    log_date = '{}Date'.format(log_type)
    df = create_dataframe_from_log(log_path, log_sheet, log_type)
    df = df.loc[(df[log_date] >= start_date) & (df[log_date] <= end_date)]
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
    get_stat_type(df, 'Sex')
    # Total by Age
    get_stat_type(df, 'Age')
    # Total Eligible
    get_stat_type(df, 'Eligible')
    # Reasons Ineligible
    get_stat_type(df, 'Reason_Ineligible')
    # Enrolled
    get_stat_type(df, 'Enrolled')
    # Reason Not Enrolled
    get_stat_type(df, 'Reason_Not_Enrolled')


def get_stat_type(df, stat_type):
    """
    Get statistics from a data frame for the given type if DataFrame contains that column
    :param df: DataFrame to get stats from
    :param stat_type: stat type to look for (i.e. Age, Gender)
    :return: No return
    """
    if stat_type == 'Age':
        if df.get('Age') is not None:
            age_stats = df['Age'].describe().to_dict()
            print_stats('Age', age_stats)
    elif df.get(stat_type) is not None:
        stat_value_counts = (df[stat_type].value_counts())
        print_stats(stat_type, stat_value_counts.to_dict())


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
    log_date = '{}Date'.format(log_type)
    log_time = '{}Time'.format(log_type)
    # Convert Date Columns
    if df.get(log_date) is not None:
        df[log_date] = df[log_date].apply(pd.to_datetime)
    # Convert Time Columns
    if df.get(log_time) is not None:
        df[log_time] = df[log_time].apply(lambda x: time(*[int(item) for item in x.split(":")]))
    # Convert Age to int
    if df.get('Age') is not None:
        df['Age'] = df['Age'].apply(pd.to_numeric)
    return df


def get_stats_by_time(log_path, log_sheet, log_type):
    df = create_dataframe_from_log(log_path, log_sheet, log_type)
    morning = time(7, 00)
    afternoon = time(12, 00)
    evening = time(16, 00)
    night = time(23, 00)
    log_time = '{}Time'.format(log_type)
    df_morning = df.loc[(df[log_time] >= morning) & (df[log_time] < afternoon)]
    df_afternoon = df.loc[(df[log_time] >= afternoon) & (df[log_time] < evening)]
    df_evening = df.loc[(df[log_time] >= evening) & (df[log_time] < night)]
    df_night = df.loc[(df[log_time] >= night) | (df[log_time] < morning)]
    # Morning Stats
    print("Stats for 07:00 to 12:00[Morning]")
    get_stats(data_frame=df_morning)
    print("-----------------------------", end="\n")
    print("Stats for 12:00 to 16:00[Afternoon]")
    get_stats(data_frame=df_afternoon)
    print("-----------------------------", end="\n")
    print("Stats for 16:00 to 23:00[Evening]")
    get_stats(data_frame=df_evening)
    print("-----------------------------", end="\n")
    print("Stats for 23:00 - 07:00[Overnight")
    get_stats(data_frame=df_night)
    return df_morning, df_afternoon, df_evening, df_night
