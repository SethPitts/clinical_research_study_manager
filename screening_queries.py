import os

import stats_functions

BASE_DIR = os.path.join(__file__)

screening_log_path = os.path.join(BASE_DIR, 'logs', 'Screening_Log.xlsx')


def get_screening_log_stats_by_date():
    start_date = input('What is the Start date [MM/DD/YYYY]? ')
    end_date = input('What is the End date [MM/DD/YYYY]? ')
    stats_functions.get_basic_stats_by_date(screening_log_path, 'Screening_log', start_date, end_date)


def get_screening_log_basic_stats():
    stats_functions.get_basic_stats(screening_log_path, 'Screening_Log')


def get_screening_log_stats_by_time():
    stats_functions.get_stats_by_time(screening_log_path, 'Screening_Log')
