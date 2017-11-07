import os

from clinical_research_study_manager import data_request_functions, stats_functions

BASE_DIR = os.path.dirname(__file__)

screening_log_path = os.path.join(BASE_DIR, 'logs', 'Screening_Log.xlsx')


def get_screening_log_stats_by_date():
    """
    Get basic stats from patients screened between two given dates
    :return: df filtered on the requested dates
    """
    start_date = data_request_functions.get_date_info('Start')
    end_date = data_request_functions.get_date_info('End')
    df = stats_functions.get_basic_stats_by_date(
        screening_log_path, 'Screening_Log', 'Screening', start_date, end_date)
    stats_functions.get_basic_plot(df, 'Screening')
    return df


def get_screening_log_basic_stats():
    """
    Get basic stats from the screening log including total screened, total by sex, age ranges,
    total eligible and reasons not eligible, total enrolled and reasons not enrolled.
    :return: No return
    """
    stats_functions.get_stats(log_path=screening_log_path, log_sheet='Screening_Log')


def get_screening_log_stats_by_time():
    """
    Get basic stats based on morning, afternoon, evening and night
    :return: No Return
    """
    stats_functions.get_stats_by_time(screening_log_path, 'Screening_Log', 'Screening')


def main():
    # get_screening_log_basic_stats()
    get_screening_log_stats_by_date()
    # get_screening_log_stats_by_time()


if __name__ == '__main__':
    main()
