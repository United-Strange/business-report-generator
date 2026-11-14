from src.excel_reader import load_sales_file
from openpyxl import Workbook
from unittest import TestCase

class TestExcelReader(TestCase):
    def test_load_sales_file(self):
        
        load_file = load_sales_file("data/input/sales.xlsx")
        
        self.assertIsInstance(load_file, Workbook)
        
        check_name = load_file.sheetnames
        self.assertIn("Sales", check_name)