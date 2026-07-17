import tkinter as tk  # 載入 Python 內建的 Tkinter 視窗介面套件

num = 2               # 要轉換的十進位數字（先設定是2）
ans = ""              # 答案 先設定成str
level = 2             # 2進位的轉換

# 轉二進位的演算法函式
def two(num, level):
    rem = ""          # 用來暫存 除法產生的餘數，最後會反向組合出最終結果的字串
    
    # 短除法原理 如果商數大於 0 時就持續進行除法運算
    while num > 0:
        # 算出當前數值除以基底的餘數
        # 將餘數轉成字串後 接到 rem 字串 的最前面（因為短除法餘數所以 由下往上讀）
        rem = (str(int((num % int(level))))) + (rem)
        
        # 進行整除後更新商數來進行下一次的計算
        num = (int(num) // int(level))
        
        print(num)    # 印出目前的商數
        print(rem)    # 印出目前累積的餘數字串
        
        show.config(text=rem)  # 將即時計算出的進位字串更新到tkinter介面上的 show Label 上


# 定義點擊按鈕後 所要做的函式
def get():
    global num        # 宣告使用全域變數 num，以便在函式內修改它
    num = get_text.get()  # 從 GUI 的輸入框（Entry）擷取使用者輸入的字串
    num = int(num)    # 將擷取到的字串轉換為整數，以便進行數學運算
    two(num, level)   # 呼叫轉換函式，並傳入數值與進位制基底開始計算


#          下面是 Tkinter 視窗介面

root = tk.Tk()             # 建立 Tkinter 的主視窗物件
root.geometry("600x600")   # 設定視窗初始大小為寬 600 像素、高 600 像素
root.title("二進位轉換器")  # 設定視窗左上角顯示的標題
root.config(bg="pink1")    # 將視窗的背景顏色設為粉紅色（pink1）

# 建立標題標籤 和 文字內容 字型大小 粉紅色背景
title = tk.Label(root, text="   二進位轉換器    \n在下面輸入數字", font=("微軟正黑體", 25), bg="pink1")
title.pack()               # 放到視窗上

get_text = tk.Entry(root, width=20)  # 建立輸入框後讓使用者輸入十進位數字
get_text.pack()            # 將他放到視窗畫面上

# 建立按鈕 當點他時 會透過 command 執行 get 函式
btn = tk.Button(root, text="完成!!!", command=get)
btn.pack()                 # 把它放置到視窗畫面上

# 建立顯示結果的標籤 一開始設為空字串且設定字型與粉紅背景
show = tk.Label(root, text="", font=("微軟正黑體", 20), bg="pink1")
show.pack()                # 將標籤放到視窗上

root.mainloop()            # 啟動 Tkinter 大迴圈

#以上都次自己寫的