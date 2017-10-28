import openpyxl

def add_patient(excel_file: str, patient_data: dict, sheet_name: str):
    """
    Add patient data to the given file
    :param excel_file: path to excel file to append data to
    :param patient_data: list of patient data to append
    :param sheet_name: sheet name to append data to
    :return: No Return
    """
    data_work_book = openpyxl.load_workbook(excel_file)
    data_sheet = data_work_book[sheet_name]
    headers = [cell.value for cell in data_sheet[1]]
    patient_data_headers = list(patient_data.keys())
    if headers == patient_data_headers:
        data_sheet.append([str(item)for item in list(patient_data.values())])
        data_work_book.save(excel_file)
    # TODO: Replace this with an exception
    else:
        print("Your headers don't you match")
        print(headers)
        print(list(patient_data_headers))
        return None
