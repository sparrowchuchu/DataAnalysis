#
import pandas as pd

# Pandas讀取 csv檔
df = pd.read_csv('fileName.csv')

# Pandas資料型態 DataFrame
data={'國語':[75,91,71,69],'數學':[62,53,88,53],'英文':[85,56,51,87],
      '自然':[73,63,69,74],'社會':[60,65,87,70],}
point=pd.DataFrame(data,index=['小林','小黃','小陳','小美'])
print(point)

print('\n後兩位的成績:')
print(point.tail(2))

print('\n將自然成績做遞減排序輸出:')
print(point.sort_values('自然',ascending=False)['自然'])

print('\n輸出第一、三位學生的數學與自然成績:')
print(point.iloc[[0,2],[1,3]])

df.head()
df.tail()
df.info()

# 
data={'name':['Bob','Nancy'],'year':[1996,1997],'month':[8,1],'day':[11,8]}
dataF=pd.DataFrame(data)
print(dataF)
print('----------------')
df1=pd.DataFrame(data,columns=['name','day','month','year','ABC'],index=['a','b'])
print(df1)

# 讀取多項資料用list[]
print(df[['Name','Team']].head(10))
# 欄位新增
df.insert(1,column='Sport',value='checked')
print(df.head())
# 欄位刪除
df=df.drop('Sport',axis=1)
print(df.head())
print('--------------')
# 刪除資料
df=df.drop(0,axis=0)
print(df.head())

df.dropna() 
df.dropna(inplace=True)
print(df)
df.dropna(subset=['欄位名稱1','欄位名稱2'])

#遮罩篩選 
mask=df['Age']>=25
print(df[mask].head(8))

mask1=df['Age'].between(20,28)
print(df[mask1].head(8))


