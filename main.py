import openpyxl as xl
import random


classes_wb = xl.load_workbook('classes.xlsx')
classes_sheet = classes_wb['Sheet1']
cell = classes_sheet.cell(2,1)


# unused
	# class_name = '' 
	# class_hours = 0
	# class_names = 1
	# classes = ''

days = ("Monday", "Tuesday", "Wednesday", "Thusday", "Friday", "Saturday", "Sunday")
hours = (1, 2, 3, 4, 5)
worksheet_to_array = []
temp_row_worksheet_to_array = []
time_table = []
professor_hours = 0
class_lessons = []
class_lessons_array = []
loop_rows = classes_sheet.max_row + 1
loop_columns = classes_sheet.max_column + 1


for row in range(2, loop_rows):
	for column in range(1, loop_columns):
		cell_value = classes_sheet.cell(row, column).value
		temp_row_worksheet_to_array.append(cell_value)
	worksheet_to_array.append(temp_row_worksheet_to_array)
	temp_row_worksheet_to_array = []

for row in worksheet_to_array:
	row_lenght = len(row)
	row_number = worksheet_to_array.index(row)
	for cell_index_p1 in range(2, row_lenght + 1):
		cell_index = cell_index_p1 - 1
		cell = row[cell_index]
		if cell_index != 0:
			loop_statement = cell_index % 2
			if loop_statement == 0:
				professor_hours += int(cell)
			else:
				professor = cell
			for hour in range(1, professor_hours+1):
				class_lessons.append(professor)
			professor_hours = 0
	class_lessons_array.append(class_lessons)
	class_lessons = []


# Debug
# print(class_lessons_array)