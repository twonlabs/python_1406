'''
# openpyl 불러오기 / 모든 기능을 불러옴
import openpyxl
'''
from openpyxl import *

# 버전 확인
# print(openpy_exam.__version__)


# == 엑셀 파일 생성, 기본 시트 선택, 셀 값 넣기 ==

# 새로운 엑셀 파일 만들기

# 새 엑셀 파일을 만들겠다 라는 의미

w1 = Workbook()

# 지금 만든 엑셀 파일을 실제 파일로 저장

w1.save('test.xlsx')

# 기존에 저장된 엑셀 파일을 다시 열어서 수정할 수 있게 함
w2 = load_workbook('test.xlsx')

# 열어온 엑셀 파일에서 첫 번째 시트 선택
ws2 = w2.active

# 셀에 값 입력하기
# A열 1행 셀에 hello라는 텍스트 입력
ws2['A1'] = 'hello'

# 변경사항 저장
# w2.save('test.xlsx')

# C열 3행 셀에 bye라는 텍스트 입력
ws2['c3'] = 'bye'

# 변경사항 저장
# w2.save('test.xlsx')

a = 'python'
# ws2[]
for row in ws2['D5' : 'F8']:
    for cell in row: # 각 행 안의 셀들을 하나씩 꺼내서
        cell.value = a # 셀에 python이라는 값 입력
         