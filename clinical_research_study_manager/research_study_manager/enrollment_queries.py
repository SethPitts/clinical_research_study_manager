import os

from research_study_manager import stats_functions, data_request_functions

BASE_DIR = os.path.dirname(__file__)

enrollment_log_path = os.path.join(BASE_DIR, 'logs', 'Enrollment_Log.xlsx')


def get_enrollment_log_stats_by_date():
    start_date = data_request_functions.get_date_info('Start')
    end_date = data_request_functions.get_date_info('End')
    df = stats_functions.get_basic_stats_by_date(
        enrollment_log_path, 'Enrollment_Log', 'Enrollment', start_date, end_date)
    stats_functions.get_basic_plot(df, 'Enrollment')


def get_enrollment_log_basic_stats():
    stats_functions.get_stats(log_path=enrollment_log_path, log_sheet='Enrollment_Log')


def get_enrollment_log_stats_by_time():
    stats_functions.get_stats_by_time(enrollment_log_path, 'Enrollment_Log', 'Enrollment')


def main():
    # get_enrollment_log_basic_stats()
    get_enrollment_log_stats_by_date()
    # get_enrollment_log_stats_by_time()


if __name__ == '__main__':
    main()
