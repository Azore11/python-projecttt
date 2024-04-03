import openpyxl
worksheet = openpyxl.load_workbook('Отметки.xlsx')
sheet = worksheet.active
two_count=0
three_count=0
four_count=0
five_count=0
for row in sheet.iter_rows(min_row=14, min_col=2, max_row=26, max_col=48):
    for cell in row:
        for i in cell.value:
            two = (cell.value).find('2')
            if two != -1:
                two_count+=1
            three = (cell.value).find('3')
            if three!=-1:
                three_count+=1
            four = (cell.value).find('4')
            if four!=-1:
                four_count+=1
            five = (cell.value).find('5')
            if five!=-1:
                five_count+=1
print(f'кол-во 2: {two_count}, кол-во 3: {three_count}, кол-во 4: {four_count}, кол-во 5: {five_count}')