import openpyxl as xl
# from array import *   # unused

classes_wb = xl.load_workbook('classes.xlsx')
classes_sheet = classes_wb['Sheet1']
cell = classes_sheet.cell(2,1)


class_name = ''
class_hours = 0
class_names = 1
classes = ''
days = ("Monday", "Tuesday", "Wednesday", "Thusday", "Fridat", "Saturday", "Sunday")
hours = (1, 2, 3, 4, 5)
worksheet_to_array = []
time_table = []

#  Debug
# print('Debug 1')

loop_rows = classes_sheet.max_row + 1
loop_columns = classes_sheet.max_column + 1


for row in range(2, loop_rows):
	# print('Debug 2')
	
	for column in range(1, loop_columns):
		worksheet_to_array = [ [[] for i in range(1, loop_columns) ] for j in range(1, loop_rows) ]

		#  Debug
		# print(f'{column}, {row}')
		# print('Debug 3')
		# print(classes_sheet.cell(row, column).value)
		
		cell_value = str(classes_sheet.cell(row, column).value)

		# DOESN'T ACTUALLY ADDS
		worksheet_to_array[row-1].extend(cell_value)

#  Debug
print(worksheet_to_array)

# for row in range(2, classes_sheet.max_row + 1):
# 	class_name = classes_sheet.cell(row, class_names).value
# 	classes += class_name + ", "
# print(classes)

# total_lessons_amount = 5

# for row in range(2, classes_sheet.max_row + 1):
# 	lessons_amount = classes_sheet.cell(row, total_lessons_amount)
