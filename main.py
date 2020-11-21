import openpyxl as xl

classes_wb = xl.load_workbook('classes.xlsx')
classes_sheet = classes_wb['Sheet1']

cell = classes_sheet.cell(2,1)

class_name = ''
class_hours = 0

class_hours = {
	class_name : class_hours ,
	'1h' : '' ,
	'2h' : '' ,
	'3h' : '' ,
	'4h' : '' ,
	'5h' : '' ,
	'6h' : '' ,
}

class_names = 1
classes = ''


for row in range(2, classes_sheet.max_row + 1):
	class_name = classes_sheet.cell(row, class_names).value
	classes += class_name + ", "
print(classes)

total_lessons_amount = 5

for row in range(2, classes_sheet.max_row + 1):
	lessons_amount = classes_sheet.cell(row, total_lessons_amount)
