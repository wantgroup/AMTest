import xlrd


def excel(fileName):
    '读取的文件的名字'
    excel = xlrd.open_workbook('/Users/cloudin/Desktop/0523.xlsx')
    sheetname = excel.sheet_names()[0]  # 获取表格的名字，不是文件名
    sheet = excel.sheet_by_index(0)  # 获取第一哥表格对象
    row_data = sheet.row_values(0)  # 获得第1行的数据列表
    col_data = sheet.col_values(0)  # 获得第一列的数据列表，然后就可以迭代里面的数据了
    cell_value1 = sheet.cell_value(0, 1)
    print(row_data)
class ReadData:
    '读取不同类型的数据'
    def __init__(self,fileName):
        pass








if __name__=="__main__":
    pass