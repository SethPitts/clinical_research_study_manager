from itertools import islice

import openpyxl
import pandas as pd

wb = openpyxl.load_workbook(
    '/home/beliefs22/PycharmProjects/clinical_research_study_manager/logs/Screening_Log.xlsx'
)
ws = wb['Screening_Log']

data = ws.values
cols = next(data)
data = list(data)
idx = [i + 1 for i, _ in enumerate(data)]
data = (islice(r, 0, None) for r in data)
df = pd.DataFrame(data, index=idx, columns=cols)
