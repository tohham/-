import tkinter as tk  # 載入 Python 內建的 Tkinter 視窗介面套件

num = 2               # 要轉換的十進位數字（先設定是2）
ans = ""              # 答案 先設定成str
level = 2             # 2進位的轉換

# 轉二進位的演算法函式
def two(num, level):
    rem = ""          # 用來暫存 除法產生的餘數，最後會反向組合出最終結果的字串
    
    # 短除法原理 如果商數大於 0 時 持續進行除法運算
    while num > 0:
        # 1. 算出當前數值除以基底的餘數
        # 2. 將餘數轉為字串後，串接到 rem 字串的「最前面」（因為短除法餘數要由下往上讀）
        rem = (str(int((num % int(level))))) + (rem)
        
        # 進行整除，更新商數以進行下一輪計算
        num = (int(num) // int(level))
        
        print(num)    # 在終端機印出目前的商數（偵錯用）
        print(rem)    # 在終端機印出目前累積的餘數字串（偵錯用）
        
        show.config(text=rem)  # 將即時計算出的進位字串更新到 GUI 介面的 show 標籤上


# 定義點擊按鈕後觸發的函式
def get():
    global num        # 宣告使用全域變數 num，以便在函式內修改它
    num = get_text.get()  # 從 GUI 的輸入框（Entry）擷取使用者輸入的字串
    num = int(num)    # 將擷取到的字串轉換為整數，以便進行數學運算
    two(num, level)   # 呼叫轉換函式，並傳入數值與進位制基底開始計算


# --- 以下為 Tkinter 視窗介面配置 ---

root = tk.Tk()             # 建立 Tkinter 的主視窗物件
root.geometry("600x600")   # 設定視窗初始大小為寬 600 像素、高 600 像素
root.title("二進位轉換器")  # 設定視窗左上角顯示的標題
root.config(bg="pink1")    # 將視窗的背景顏色設為粉紅色（pink1）

# 建立上方的主標題標籤，設定文字內容、字型大小，並融入粉紅色背景
title = tk.Label(root, text="   二進位轉換器    \n在下面輸入數字", font=("微軟正黑體", 25), bg="pink1")
title.pack()               # 將標題標籤放置並對齊到視窗畫面上

get_text = tk.Entry(root, width=20)  # 建立單行文字輸入框，供使用者輸入十進位數字
get_text.pack()            # 將輸入框放置到視窗畫面上

# 建立執行按鈕，當使用者點選時，會透過 command 參數觸發執行 get 函式
btn = tk.Button(root, text="完成!!!", command=get)
btn.pack()                 # 將按鈕放置到視窗畫面上

# 建立用來顯示轉換結果的標籤，初始文字為空字串，並設定字型與粉紅背景
show = tk.Label(root, text="", font=("微軟正黑體", 20), bg="pink1")
show.pack()                # 將結果標籤放置到視窗畫面上

root.mainloop()            # 啟動 Tkinter 的事件監聽大迴圈，讓視窗保持顯示並偵測使用者操作

#以上都次自己寫的