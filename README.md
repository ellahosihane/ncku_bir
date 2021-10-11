# BIR_Project 1 Full-text retrieval tool
生醫資訊作業
# Dependencies
* Python 3.7.11
* Pyqt5 5.15.4
# GUI
1. 使用Qt Designer 設計介面
2. 使用VScode 的 PYQT Integration extensiont對fulltext.ui進行編譯，生成對應的Ui_fulltext.py
 ![image](https://user-images.githubusercontent.com/91927076/136767797-d928d97d-e9fb-4665-b2d5-e974396aa6e3.png)
# Demo
* python main.py
* 輸入檔案路徑或點選...選擇檔案(可選擇XML與JSON格式)
 ![image](https://user-images.githubusercontent.com/91927076/136768404-6c3d2310-1543-4c63-8a30-d4cf0a6c5eba.png)
* 點選Load讀取文件
  * 顯示格式仿照PubMed與Twitter，並於左下角顯示當前內容的字元數、字數與句數
  * xml格式預設顯示檔案中首篇文章，點選左方清單可選擇其他文章
  * json格式則是全數顯示
 ![image](https://user-images.githubusercontent.com/91927076/136770259-9a4e7959-a3c5-41d7-a8e7-cee76b357046.png)
 ![image](https://user-images.githubusercontent.com/91927076/136769722-55c9f991-16a2-4241-be2a-4533e4007e0d.png)

* Text Search
![image](https://user-images.githubusercontent.com/91927076/136770708-fded8631-d96f-41d8-af09-925003e1c66d.png)

# Reference
[VSCode + PYQT5 + QtDesigner 環境搭建和測試](https://www.itread01.com/content/1541809161.html)
