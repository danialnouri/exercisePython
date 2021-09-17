from openpyxl import workbook
wb = workbook()
ws = wb.activate()
ws1=wb.create_sheet ('my sheet')
ws1.title = 'new title'

