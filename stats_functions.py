from itertools import islice

import openpyxl
import pandas as pd


def get_basic_stats_by_date(log, log_sheet, start_date, end_date):
    # Total Subjects between dates
    # Count by Sex, Age
    # Total eligible
    # Total not eligible
    # Reason for ineligible
    # Total Enrolled
    # Total Not enrollment
    # Reason for not enrolled
    return None


def get_basic_stats(log, log_sheet):
    # Total Subjects in the log
    # Count by Sex, Age
    # Total eligible
    # Total not eligible
    # Reason for ineligible
    # Total Enrolled
    # Total Not enrollment
    # Reason for not enrolled
    work_book = openpyxl.load_workbook(log)
    work_sheet = work_book[log_sheet]
    data = work_sheet.values
    col_names = next(data)  # Get Headers as column name
    log_data = list(data)
    row_ids = [i for i, _ in enumerate(log_data)]  # Get count of subjects in file as row_id
    log_data = (islice(row, 0, None) for row in log_data)
    df = pd.DataFrame(log_data, index=row_ids, columns=col_names)
    # Total subjects
    total_subjects_in_log = len(df)
    # Total by Sex
    if df.get('Sex') is not None:
        sex = (df['Sex'].value_counts())
        print("Sex Stats")
        print(sex.to_dict())
    # Total by Age
    if df.get('Age') is not None:
        print("age stats")
        age = (df['Age'].value_counts())
        print(age.to_dict())
    # Total Eligible
    if df.get('Eligible') is not None:
        print(df['Eligible'].value_counts())
    # Reasons Ineligible
    if df.get('Reason_Ineligible') is not None:
        print(df['Reason_Ineligible'].value_counts())
    # Enrolled
    if df.get('Enrolled') is not None:
        print(df['Enrolled'].value_counts())
    # Reason Not Enrolled
    if df.get('Reason_Not_Enrolled') is not None:
        print(df['Reason_Not_Enrolled'].value_counts())
    return None


def get_stats_by_time(log, log_sheet):
    # Morning (7am-12pm) - Afternoon-Evening(12pm-11pm) -Overnight(11pm-7am)
    # Total Subjects at times
    # Count by Sex, Age
    # Total eligible
    # Total not eligible
    # Reason for ineligible
    # Total Enrolled
    # Total Not enrollment
    # Reason for not enrolled
    return None
