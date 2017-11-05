import os
from itertools import islice

import openpyxl
import pandas as pd


def testing_pandas():
    BASE_DIR = os.path.dirname(__file__)
    wb = openpyxl.load_workbook(os.path.join(BASE_DIR, 'logs', 'Screening_Log.xlsx'))
    ws = wb['Screening_Log']
    data = ws.values
    cols = next(data)
    data = list(data)
    idx = [i + 1 for i, _ in enumerate(data)]
    data = (islice(r, 0, None) for r in data)
    df = pd.DataFrame(data, index=idx, columns=cols)
    df[['ScreeningDate']] = df[['ScreeningDate']].apply(pd.to_datetime)
    df[['Age']] = df[['Age']].apply(pd.to_numeric)
    return df


def main():
    df = testing_pandas()
    print(df)


if __name__ == '__main__':
    main()
