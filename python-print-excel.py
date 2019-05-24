#
# https://stackoverflow.com/questions/49271943/how-to-print-all-column-values-from-excel-using-python
#import openpyxl
"""
print('test')
from openpyxl import load_workbook
book = load_workbook('test.xlsx')
sheet = book['Sheet1']

for row in sheet.rows:
    print(row[1].value)
"""

# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("test.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
# print(sheet.cell_value(0, 0))
for i in range(13):
    print(sheet.cell_value(i, 0))
    number = sheet.cell_value(i, 0)
    if number < 5:
        print("OH MY GOSH!")
