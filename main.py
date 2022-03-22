import openpyxl
import datetime

excel_file = openpyxl.load_workbook('lessons.xlsx')
cl = excel_file['Лист1'].cell(row=1, column=5)
for y in range(5,  excel_file['Лист1'].max_column+1):
    for x in range(2, 12):
        lesson = excel_file['Лист1'].cell(row=x, column=5).value
        time = excel_file['Лист1'].cell(row=x, column=1).value
        if lesson != None:
            print(lesson)
            print(time)
        else:
            print(f'Сейчас у {cl.value} нету урока :)')
