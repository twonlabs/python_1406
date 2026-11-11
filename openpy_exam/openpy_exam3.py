from openpy_exam import *
from openpy.styles import PatternFill

wb = Workbook()
ws = wb.active


# 헤더
ws['A1'] = '이름' 
ws['B1'] = '국어'
ws['C1'] = '수학'

color = PatternFill(fill_type='solid', fgColor='FFFF00')

# 반복문을 통해 셀의 배경색 바꾸기
for cell in ws[1]: # 1행 전체
    cell.fill = color

    