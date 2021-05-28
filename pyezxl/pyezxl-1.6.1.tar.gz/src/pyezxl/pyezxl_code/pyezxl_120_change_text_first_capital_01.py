#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("")
sheet_name = excel.read_activesheet_name()
[x1, y1, x2, y2] = excel.read_select_address()

for x in range(x1, x2+1):
	for y in range(y1, y2+1):
		cell_value = str(excel.read_cell_value(sheet_name,[x, y]))
		if cell_value == "None" : cell_value = ""

		#여기 위까지는 선택한 영역을 하나씩 돌아가는 코드이다
		changed_cell_value = cell_value.capitalize()


		excel.write_cell_value(sheet_name, [x, y], changed_cell_value)