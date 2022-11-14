# 
import numpy as np

# numpy 常用數學函數
array=np.random.randint(1,21,size=20)
print('隨機正整數:',array)
print('X矩陣內容: \n',array.reshape(5,4))
print('最大: ',array.max())
print('最小: ',array.min())
print('平均: ',array.mean())
print('總和: ',array.sum())
print('標準差: ',array.std())
print('四個角落元素: \n',array.reshape(5,4)[np.ix_([0,4],[0,3])])

# 二維串列轉陣列
data=[[1,2,3,4,5],[6,7,8,9,10]]
array1=np.array(data)
print(array1)

# dtype設定元素型態
array2=np.array(data,dtype=float)
array3=np.array(data,dtype=bool)
print(array2)
print(array3)

# 三維串列轉陣列
data3D=[[[0,1],[2,3],[4,5]],[[1,1],[2,3],[4,5]],[[2,1],[2,3],[4,5]]]
array3D=np.array(data3D)

a=np.array([[3,6,9],[2,4,6]])

print('ndim:',a.ndim)
print('shape:',a.shape)
print('type:',type(a))
print('dtype:',a.dtype)
print('data:',a.data)
print('T\n',a.T,'\n')
print(a)
print('size:',a.size)
print('itemsize:',a.itemsize)
print('nbytes:',a.nbytes)
print('strides:',a.strides)  #步長

#回傳累積的數值
a.cumsum() 

#取標準差
np.std(a)

#array內不可有空格
b=np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])

# .ix 可將特定列、欄 交叉點位置元素取出
z=b[np.ix_([2,4],[0,2,4])]

