import mysql.connector
import xlrd

conn=mysql.connector.connect(host="localhost", user="root",passwd="computer",data="sundeep")
cur=conn.cursor()
loc=("C:\\Users\\jeffr\\OneDrive\\Desktop\\student.xlsx")
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,21):
    print(tuple(sheet.row_values(i)))

conn.close()