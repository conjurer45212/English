import xlrd
import random

wb = xlrd.open_workbook('english.xlsx')
sheet = wb.sheet_by_name('Sheet2')

word_e = {}
word_j = {}
number = len(sheet.col_values(0))

def CreateRandom(n):
    y = []
    for i in range(1,n):
        y.append(i)
    random.shuffle(y)
    return y

for i in range(number):
    if i > 0:
        cell_e = sheet.cell(i,0)
        cell_j = sheet.cell(i,1)
        word_e[i] = cell_e.value
        word_j[i] = cell_j.value

count = 1
point = 0
que_num = 100
for i in range(que_num):
    print("-"*10+"問題",count,"-"*10)
    create = CreateRandom(number)
    temp1 = create[0]
    temp2 = create[1]
    temp3 = create[2]
    temp4 = create[3]

    temp_ans = random.randint(1,4)
    if temp_ans == 1:
        ans = temp1
    if temp_ans == 2:
        ans = temp2
    if temp_ans == 3:
        ans = temp3
    if temp_ans == 4:
        ans = temp4

    print(word_e[ans])
    print("1." + word_j[temp1] + " " + "2." + word_j[temp2] + " " +
          "3." + word_j[temp3] + " " + "4." + word_j[temp4])
    answer = input("answer  -->")
    if temp_ans == int(answer):
        print("正解")
        point = point + 1
    else:
        print("不正解")
        print("正解: " + word_j[ans])
    count = count + 1

print("-"*27)
print("正解数: " + str(point) + "/" + str(que_num))
