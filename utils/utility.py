from openpyxl import load_workbook
from COSTANTS import FILE_PATH

def open_wb(wb):
    wb.append(load_workbook(f'{FILE_PATH}'))
