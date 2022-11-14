# csv 資料格式
import csv

# reader() 
# Python預設是ANSI編碼
with open('fileName.csv',encoding='utf-8-sig') as csvfile:
    csvReader=csv.reader(csvfile)
    listReport=list(csvReader)

# writer()  
# delimiter='\t'
with open('fileName.csv','w',newline='') as csvfile:
    csvWriter=csv.writer(csvfile)
    for row in listReport:
        csvWriter.writerow(row)


