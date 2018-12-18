import xlrd


def get_excel_data():
    workbook = xlrd.open_workbook("DataEngine.xls")
    sheet = workbook.sheet_by_name("DataSheet")

    column_values = sheet.col_values(3)
    column_values = column_values[1:]
    return column_values


if __name__ == "__main__":
    get_excel_data()
