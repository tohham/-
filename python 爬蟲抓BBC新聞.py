import requests
import tkinter as tk 
from bs4 import BeautifulSoup
from tkinter.scrolledtext import ScrolledText #滾動式字
#加入這次專案的所需的模組

url = "https://feeds.bbci.co.uk/zhongwen/trad/rss.xml" #這個是要訪問的網站 p.s(要取得的資料)
my_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}#提供我的訪問資料
response = requests.get(url,headers = my_headers)   #訪問網站
if response.status_code == 200:                         #網站回傳值(如果=200那麼就代表 允許訪問)
    soup = BeautifulSoup(response.text,'xml')         #我要解析的方法模式
    item = soup.find_all('item')    #找出所有item的標籤 
    print(f"共抓了{len(item)}則新聞")   #找出有幾篇
    ans = ""    #讓程式先設定,一個ans變數並把它的性質變成str,使後面要增加第一次時,可以正常運作
    for itm_out in item:    #把item這一大串標籤給一個個拆開
        title =itm_out.find("title").text   #在item_out裡面找出"<title>"的東西 .text可以除掉不是 "字串文字" 的東西
        in_word = itm_out.find("description").text  #在item_out裡面找出"<description>"的東西
        ans = (f"標題:\n {title}\n\n(副標題):\n {in_word}\n\n\n---------------------------------------------------------------------------------------------------\n\n\n")+(ans)
        #字串文字編輯 f"" 是動態文字
else:
    print("BBC網站目前連接不上")#萬一回傳數值報錯
    ans = "無法連接到 BBC 新聞伺服器，請檢查網路連線"#提醒網路有沒有開啟
        
root = tk.Tk()
root.geometry("600x800")
root.configure(bg="blue3")
root.title("每日大事件!!!!!")
#tkinter視窗基本資料

tk_text = ScrolledText(bg="blue3",fg = "white",font=("Microsoft JhengHei", 14, "bold"))#視窗裡 ScrolledText 可使tkinter視窗有上下滑動滾輪
tk_text.pack(fill="both",expand=True)#讓字串空間排好何讓使用者可以自由放大縮小頁面

tk_text.insert(tk.END,ans) #把ans文字 加進tk_text 的最後端
tk_text.config(state=tk.DISABLED)   #使 使用者進入 只能閱讀不能修改的模式

root.mainloop()#使視窗有可動性     註解皆由本人寫的!

