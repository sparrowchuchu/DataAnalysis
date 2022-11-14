#
import pandas as pd
import sqlite3
 
# Connect Databace
def connectDB(dbName:str,table:str,column:str,clause:str=None):
    conn=sqlite3.connect(f'{dbName}')
    print(f'Opened {dbName} successfully.')
    sql=f'SELECT {column} FROM {table} WHERE {clause}'
    print('Execute: '+sql)
    data=conn.execute(sql).fetchall()  # fetchall()：取出全部資料
    conn.close()
    print(f'Closed {dbName} successfully.')
    return [i[0] for i in data] 
 
 
# 讀取CSV資料集檔案 
df = pd.read_csv('Billionaire.csv') 

# 建立資料庫
conn = sqlite3.connect('billionaire.db')  
cursor = conn.cursor()
# 建立資料表
cursor.execute('CREATE TABLE Billionaire(Name, NetWorth, Country, Source, Rank)')  
conn.commit()
 
# 如果資料表存在，就寫入資料，否則建立資料表
df.to_sql('Billionaire', conn, if_exists='append', index=False) 
 
# 透過SQL語法讀取資料庫中的資料
us_df = pd.read_sql("SELECT * FROM Billionaire WHERE Country='United States'", conn)
print(us_df)

# 關閉資料庫
conn.close()
print('Closed DataBace successfully')

# 實用 pandas 資料清洗方法
# 刪除行
df.drop(column, axis=1, inplace=True)

# 重新命名行
df.rename(index={'row1':'A'},columns ={'col1':'B'})

# 缺失值處理Python版
df.fillna(value = 0)
df1.combine_first(df2)











