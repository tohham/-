(請按 Window + R 輸入 cmd 開啟 執行以下指令來下載套件)

  安裝網頁爬蟲、XML 解析與 YOLO 核心套件：
pip install requests beautifulsoup4 lxml ultralytics

  安裝顯卡加速：#不想安裝 看下面
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

    注意
  第一次執行 YOLO 辨識時程式會自動聯網下載模型檔不需手動下載。
  測試電腦 沒有顯卡 或 不想安裝加速檔案 請將程式碼中的 device="cuda" 改為 device="cpu"，並把 model = YOLO("yolo11x.pt") 改成 YOLO("yolov8m.pt")。這樣做能避免畫面卡頓 但會犧牲辨識精準度
  感謝:>
