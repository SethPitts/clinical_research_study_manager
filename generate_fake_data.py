import random
from collections import OrderedDict

options = dict()
letters = []
get_int = lambda x, y: random.randint(x, y)
options['sex'] = ['M', 'F', 'U']
options['yes_no_unknown'] = ['Y', 'N', 'U']
options['yes_no_na'] = ['Y', 'N', 'NA']
options['reasons_not_eligible'] = ['unconsentable', 'does_not_meet_criteria', 'previously_enrolled', 'NA']
options['reasons_not_enrolled'] = ['declined', 'NA']
options['mrn'] = list(range(10000000, 20000000))
options['age'] = list(range(1, 100))
options['date'] = ['{}/{}/{}'.format(get_int(1, 12),
                                     get_int(1, 28),
                                     get_int(2012, 2016)
                                     )
                   ]
options['time'] = ['{}:{}'.format(get_int(0, 23),
                                  get_int(0, 59)
                                  )
                   ]
options['initials'] = ['{}{}{}'.format(chr(get_int(97, 122)),
                                       chr(get_int(97, 122)),
                                       chr(get_int(97, 122))
                                       )
                       ]
options['subject_id'] = [get_int(1, 1000)]
options['enrollment_arm'] = ['arm1', 'arm2']
options['name'] = ['jane', 'doe', 'bob', 'marley']


def get_screening_headers():
    screening_headers = OrderedDict()
    screening_headers['Screening_Date'] = 'date'
    screening_headers['Screening_Time'] = 'time'
    screening_headers['Subject_Initials'] = 'initials'
    screening_headers['Medical_Record_Number'] = 'mrn'
    screening_headers['Age'] = 'age'
    screening_headers['Sex'] = 'sex'
    screening_headers['Eligible'] = 'yes_no_unknown'
    screening_headers['Reasons_Ineligible'] = 'reasons_not_eligible'
    screening_headers['Enrolled'] = 'yes_no_na'
    screening_headers['Reason_Not_Enrolled'] = 'reasons_not_enrolled'
    screening_headers['Research_Assistant_Initials'] = 'initials'
    return screening_headers


def get_enrollment_headers():
    enrollment_headers = OrderedDict()
    enrollment_headers['Subject_ID'] = 'subject_id'
    enrollment_headers['Enrollment_Date'] = 'date'
    enrollment_headers['Enrollment_Time'] = 'time'
    enrollment_headers['Age'] = 'age'
    enrollment_headers['Sex'] = 'sex'
    enrollment_headers['Enrollment_Arm'] = 'enrollment_arm'
    enrollment_headers['Research_Assistant_Initials'] = 'initials'
    return enrollment_headers


def get_follow_up_headers():
    follow_up_headers = OrderedDict()
    follow_up_headers['Subject_ID'] = 'subject_id'
    follow_up_headers['Enrollment_Date'] = 'date'
    follow_up_headers['Enrollment_Time'] = 'time'
    follow_up_headers['Follow_Up_Date'] = 'date'
    follow_up_headers['Follow_Up_Time'] = 'time'
    follow_up_headers['Follow_Up_Complete'] = 'yes_no_na'
    follow_up_headers['Notes'] = 'yes_no_na'
    return follow_up_headers


def get_linking_log_headers():
    linking_headers = OrderedDict()
    linking_headers['Subject_ID'] = 'subject_id'
    linking_headers['Medical_Record_Number'] = 'mrn'
    linking_headers['Enrollment_Date'] = 'date'
    linking_headers['Enrollment_Time'] = 'time'
    linking_headers['Subject_Name'] = 'name'
    linking_headers['Age'] = 'age'
    linking_headers['Sex'] = 'sex'
    linking_headers['Research_Assistant_Initials'] = 'initials'
    return linking_headers


def generate_patient_dict(data_headers: OrderedDict) -> OrderedDict:
    patient_dict = OrderedDict()
    for header, data_type in data_headers.items():
        patient_dict[header] = random.choice(options[data_type])
    return patient_dict


def main():
    screening_dict = generate_patient_dict(get_screening_headers())
    enrollment_dict = generate_patient_dict(get_enrollment_headers())
    follow_up_dict = generate_patient_dict(get_follow_up_headers())
    linking_dict = generate_patient_dict(get_linking_log_headers())

    data_dicts = [screening_dict, enrollment_dict, follow_up_dict, linking_dict]

    for data_dict in data_dicts:
        for item, value in data_dict.items():
            print(item, value, sep=":")
        print("---------------------------------------")


if __name__ == '__main__':
    main()
