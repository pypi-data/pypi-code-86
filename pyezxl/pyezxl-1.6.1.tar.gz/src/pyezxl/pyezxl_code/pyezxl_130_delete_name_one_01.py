#  -*- coding: utf-8 -*-

import pyezxl
excel = pyezxl.pyezxl("activeworkbook")

#현재 화일에서 이름을 삭제하는것
input_text=excel.read_messagebox_value("Please input text")
excel.delete_sheet_rangename(input_text)
