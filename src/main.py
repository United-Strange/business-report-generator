from src.excel_reader import load_sales_file
from src.sheet_selector import sheet_selector

workbook = load_sales_file("data/input/sales.xlsx")

selected_sheet = sheet_selector(workbook)