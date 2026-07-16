from ultralytics import YOLO #我要先載入這次所需的程式

model = YOLO("yolo11x.pt")#這我要使用的是YOLO (yolo是利用AI視覺辨識系統來辨識圖片)
requests = model.track(source="0",show = True,
                        imgsz = 1280,classes = [43,76],
                        conf = 0.65,stream=True,device="cuda")
                        #source="0" 他的意思是使用我的電腦螢幕攝像頭來拍東西
                        #show = True 意思是開啟攝像頭拍到的畫面(視窗)
                        #imgsz = 1280 這意思是讓從攝像頭拍到的東西 變成1280解析度
                        #classes = [43,76] 的意思是讓他只檢測 他們資料庫 43(刀刃) 和 76(剪刀)
                        #conf = 0.65 這個代表他的辨識正確的信心程度>65%他才會抓
                        #stream = True 辨識完後就讓它消失 才不會讓暫存資料多到爆炸
                        #device = "cuda" 用我的顯卡跑 萬一用我的cpu跑這個會很卡


for r in requests:#用for迴圈來處理他給得的畫面
    box= r.boxes #讓boxes變數儲存 處裡好(r)的資料
    if len(box) > 0: #如果畫面的物品>0那
        for bx in box:
            id =int(bx.cls[0])#讓id等於他檢測到的物品
            if id == 76: #如果是剪刀 那寫剪刀
                print("剪刀")
            if id == 43:#如果是刀 那就寫刀
                print("刀刃") 