#
import yfinance as yf

stock=yf.Ticker("2330.TW")

df=stock.history(period="max")
# df=stock.history(start="2022-01-01",end="2022-08-03")

# 股票基本資訊
dfInfo=stock.info

# 內部人士與機構法人持有比例
majorHolders=stock.major_holders

# 主要持有機構法人
insHolders=stock.institutional_holders

# 資產負債表
blanceData=stock.blance_sheet

# 現金流量表
cfData=stock.cashflow

# 分析師建議 (目前僅有美股資料)
reCommend=stock.recommendations

