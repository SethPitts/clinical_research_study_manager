from itertools import islice

import openpyxl
import pandas as pd

wb = openpyxl.load_workbook('../logs/Screening_Log.xlsx')
ws = wb['Screening_Log']

data = ws.values
cols = next(data)
data = list(data)
idx = [r[0] for r in data]
data = (islice(r, 0, None) for r in data)
df = pd.DataFrame(data, index=idx, columns=cols)
print(df.keys())
