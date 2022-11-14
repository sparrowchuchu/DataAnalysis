#
import requests
import re

url=input('輸入網址: ')
htmlfile=requests.get(url)
if htmlfile.status_code==200:
    pattern=input('要搜尋的字串: ')
    if pattern in htmlfile.text:
        print('搜尋%s成功'%pattern)
    else:
        print('搜尋%s失敗'%pattern)
    # 計算出現次數
    name=re.findall(pattern,htmlfile.text)
    if name!=None:
        print('%s出現%d次'%(pattern,len(name)))
    else:
        print('%s出現 0 次'%pattern)
else:
    print('網頁下載失敗')
        
        
        