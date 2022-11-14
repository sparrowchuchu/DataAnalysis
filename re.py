
import re

key1="abcde@abc.edu.tw   fggggg@ooo.com.tw   fghijk@ooo.com.jp   fghijk@ooo.com.tw"
key2="02-56558878"

p1="(.@.+.tw$){1}"
p2="@.+."
pEmail="\w+@\w+\.\w+\.tw"  # 正則搜尋 e-mail
pPhoneTel="\d{2}-\d{8}"    # 正則搜尋 室內電話號碼

pattren1=re.compile(p1)
pattren2=re.compile(p2)
print(pattren1.findall(key1))
print(pattren2.findall(key1))

re.findall(pEmail,key1)

# findall(string,[,pos[,endpos]])
   # string:帶匹配字串，pos:字串起始位置(預設為0)，endpos:字串結束位置(預設為字串長度)

# match()

# search() 回傳第一筆比對相符的字串

r"""
正則表達式 Regular Expression
特殊字元:
    .       任意字元
    \d      十進位數字[0-9]
    \D      非 十進位數字[^0-9]
    \s      空白 [\t\n\xOB\f\r]
    \S      非 空白 [^\t\n\xOB\f\r]
    \b      字的界限 如空白
    \B      非 字的界限
    \w      字母、數字或底線 [a-zA-Z0-9_]
    \W      非 字母、數字或底線 [^a-zA-Z0-9_]
    ^       字首 (放置在 re起始位置)
    $       字尾 (放置在 re末端)
    \       跳脫字元

量次:
    ?       0 至 1次     
    *       0 至 多次
    +       1 至 多次
    {n}     n次
    {,m}    0 至 m次
    {n,m}   n 至 m次

設定字元區間:  
    [a-z]   a-z小寫字元
    [2-5]   2-5的數字    
    [^a-z]  不在 a-z中的字元
    [rabbit|fox]     分隔樣式符號

"""
