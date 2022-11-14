# requests，bs4。
import requests
from bs4 import BeautifulSoup


headers={"User-Agent":
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

ResponseObject=requests.get("https://www.xxxxxx",headers=headers)

if ResponseObject.status_code==200:
    print("成功讀取")
else:
    print("讀取失敗")

soup=BeautifulSoup(ResponseObject.text,'lxml')

soup.prettify()  #排版 html格式文字

soup.title       #網頁標題屬性
soup.a.text      #取得網頁標籤<a>的值
soup.find("a")
soup.find(id="xxx")
soup.find(class_="xxx")
soup.find(class_="xxx").text

soup.find("a",{"id":"xxx"})
soup.find("a",{"href":"https://www.xxxxxx"})

soup.find("a",{"id":"xxx"}).get("href") #取得<a>標籤 href的內容

soup.get_text()

# select 會傳回串列
soup.select(".xxx")   # . == class
soup.select("#xxx")   # # == id



