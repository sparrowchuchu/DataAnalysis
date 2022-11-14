# json資料格式: []陣列，{"key":"value"}物件
import json

# load() 
# 讀取 json檔案，轉成 Python資料格式
with open("fileName") as jsonFile:
    data=json.load(jsonFile)

# dump() 
# 將 Python資料格式 轉成 json物件 或是 json陣列(副檔名是json)。
with open("fileName.json","w") as jsonFile:
    json.dump(data,jsonFile)


# json資料格式: []陣列，{"key":"value"}物件
meals={'breakfast':50,'lunch':80,'dinner':100}

