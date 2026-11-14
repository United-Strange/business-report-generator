from openpyxl import load_workbook

def load_sales_file(file_path):
    workbook = load_workbook(file_path)
    return workbook