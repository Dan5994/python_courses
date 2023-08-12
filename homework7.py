# Задание 1


got = b'r\xc3\xa9sum\xc3\xa9'
hou = got.decode()
print(hou)
gur = hou.encode("Latin1")
print(gur)


# Задание 2
word_1='Привет'
word_2='это'
word_3='первая запись'
word_4='в файл'

fon=open('dop7.txt','w')
fon.write(word_1 + ' ')
fon.write(word_2 + ' ')
fon.close()

with open ('dop7.txt','a') as dop:
    dop.write(word_3 + ' ')
    dop.write(word_4)


# # Задагие 3
import json


com_dict = {
    356283:('Dan', 25),
    638025:('Jon', 28),
    545433:('Bob', 18),
    943642:('Lina', 22),
    638323:('Alex', 30),
    638065:('Mark', 19),
}

with open ('dop_f.json', 'w') as hol:
    json.dump(com_dict,hol)


# Задание 4
import csv

with open ('dop_f.json', 'r') as file_j:
        output=json.load(file_j)
        with open ('dop_csv.csv', 'w') as csv_f:
                fieldnames = ['Id', 'Name' , 'Age' , 'Number']
                writer = csv.DictWriter(csv_f,fieldnames=fieldnames)
                writer.writeheader()
                for id, lis in output.items():
                    name = lis[0]
                    age = lis[1]
                    writer.writerow({'Id':id ,'Name':name , 'Age':age , 'Number':''})

# Задание 5
# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# with open ('dop_csv.csv', 'r') as csv_f:
      