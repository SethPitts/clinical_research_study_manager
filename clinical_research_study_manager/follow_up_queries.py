import datetime
import os

import pandas as pd
from clinical_research_study_manager.data_request_functions import get_date_info
from clinical_research_study_manager.stats_functions import create_dataframe_from_log

BASE_DIR = os.path.dirname(__file__)

follow_up_log_path = os.path.join(BASE_DIR, 'logs', 'Follow_Up_Log.xlsx')


def follow_up_by_custom_dates():
    """
    Find follow ups between a two dates
    :return: DataFrame filter on the two dates
    """
    start_date = get_date_info('Follow Up Start')
    end_date = get_date_info('Follow Up End')
    follow_up_df = follow_ups_scheduled_between_dates(start_date, end_date)
    print("You have {} follow Ups scheduled between {} and {}".format(len(follow_up_df), start_date, end_date))
    print(follow_up_df.head())
    return follow_up_df


def follow_ups_scheduled_for_today():
    """
    Get Follow Ups Scheduled for Today
    :return: DataFrame filtered on today
    """
    today = pd.to_datetime(datetime.date.today())
    type(today)
    follow_up_df = follow_up_scheduled_on_date(today)
    print("You have {} follow ups scheduled for today".format(len(follow_up_df)))
    print(follow_up_df)
    return follow_up_df


def follow_ups_scheduled_for_this_week():
    """
    Get Follow Ups scheduled for this week
    :return:  DataFrame filtered on today
    """
    start_of_week = pd.to_datetime(datetime.date.today())
    end_of_week = pd.to_datetime(datetime.date.today() + datetime.timedelta(7))
    follow_up_df = follow_ups_scheduled_between_dates(start_of_week, end_of_week)
    print("You have {} follow ups scheduled for this week".format(len(follow_up_df)))
    print(follow_up_df.head())
    return follow_up_df


def follow_up_scheduled_on_date(follow_up_date):
    """
    Create follow up DataFrame filtered on a specific date
    :param follow_up_date: date to filter the DataFrame on
    :return: Filtered DataFrame
    """
    follow_up_df = create_dataframe_from_log(follow_up_log_path, 'Follow_Up_Log', 'FollowUp')
    today_df = follow_up_df.loc[(follow_up_df.FollowUpDate == follow_up_date)]
    return today_df


def follow_ups_scheduled_between_dates(start_date, end_date):
    """
    Create Follow up DataFrame filtered between two dates
    :param start_date: start date to filter on
    :param end_date: end date to filter on
    :return: Filtered DataFrame
    """
    follow_up_df = create_dataframe_from_log(follow_up_log_path, 'Follow_Up_Log', 'FollowUp')
    week_df = follow_up_df.loc[(follow_up_df.FollowUpDate >= start_date) & (follow_up_df.FollowUpDate <= end_date)]
    return week_df


def patients_at_risk_of_being_lost():
    """
    Create Follow up data frame for at risk subjects
    :return: DataFrame containing subjects at risks of being lost to follow up
    """
    today = pd.to_datetime(datetime.date.today())
    follow_up_df = create_dataframe_from_log(follow_up_log_path, 'Follow_Up_Log', 'FollowUp')
    at_risk_df = follow_up_df.loc[(follow_up_df.FollowUpDate < today) &
                                  (follow_up_df.FollowUpComplete == 'N')]
    print("There are {} subjects at risk of being lost".format(len(at_risk_df)))
    print(at_risk_df.head())
    return at_risk_df


def main():
    # follow_ups_scheduled_for_today()
    # patients_at_risk_of_being_lost()
    # follow_ups_scheduled_for_this_week()
    follow_up_by_custom_dates()


if __name__ == '__main__':
    main()
