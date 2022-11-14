# xml
import xml.etree.ElementTree as et

tree=et.parse('fileName.xml')    # 解析xml，回傳 ElementTree物件
root=tree.getroot()              # 獲得根結點
for child in root:               # 用for迴圈讀取xml樹狀結構資料
    print('tag:',child.tag,'attribute:',child.attrib)
    for grandchild in child:
        print('tag:',grandchild.tag,'attribute:',grandchild.attrib)
print(list(root))
print(len(root))
print(root)


cdtree=et.parse('country_data.xml')
cdroot=cdtree.getroot()
for country in cdroot.findall('country'):
    rank=int(country.find('rank').text)
    if rank>50:
        root.remove(country)
tree.write('xmloutpute.xml',encoding='utf8')


#%% 29號同學的筆記
#利用ElementTree()函數讀取檔案,並建立名為tree的物件
tree =et.ElementTree(file='menu.xml')

#運用tree物件皫getroot()函式建立名為root的物件
root =tree.getroot()

#輸出root物件的tag屬性(得到menu)
print(root.tag)

#使用廻圈尋找root物件的child子節點,並輸出tag與attrib屬性
for child in root:    
    print('tag:',child.tag,'attributes',child.attrib)
    ##使用廻圈尋找child物件的子(孫)節點,並輸出tag與attrib屬性
    for grandchild in child:        
        print('\ttag',grandchild.tag,'attributes',grandchild.attrib)