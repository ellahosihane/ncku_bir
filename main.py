import sys
import os
import xml.etree.ElementTree as ET
import json
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget, QLabel, QWidget
from PyQt5.QtGui import *
from Ui_fulltext import Ui_MainWindow  

class SubWindow(QWidget):
     def __init__(self):
         super(SubWindow, self).__init__()
         self.resize(400, 300)

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.Choose.clicked.connect(self.ChooseClicked)
        self.Search.clicked.connect(self.FindClicked)
        self.Parse.clicked.connect(self.ParseClicked)
        self.DoclistWidget.itemClicked.connect(self.ItemClicked)
        self.cwd = os.getcwd()
        self.filename = os.getcwd()
        self.Statistics = {}
        self.itemList = []
        self.contentList = {}
        self.itemList = 0
    
    def ChooseClicked(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, "選取文件",self.cwd,"XML Files(*.xml);;JSON Files(*.json)")
        self.Filepath.setText(self.filename[0])

    def ParseClicked(self):
        if self.filename[0].endswith(".xml") or self.filename[0].endswith(".json"): 
            self.Read()
            self.itemList = [_ for _ in self.contentList.keys()]
            self.DoclistWidget.addItems(self.itemList)
            self.DoclistWidget.setCurrentRow(0)
            self.ItemClicked()
        else:
            print('The file format or file extension is not valid.')
        # self.TextBrowser.append(self.contentList[self.itemList[0]])

    def FindClicked(self):
        wordList = list(self.contentList[self.itemList[self.item_index]])
        curr_content = self.contentList[self.itemList[self.item_index]]
        keyword = self.KeyWord.text()
        index_list = []
        if keyword != "":
            index_list.extend([_.start() for _ in re.finditer(keyword.lower(), curr_content.lower())])
        for num, index in enumerate(index_list):
            wordList.insert(index + num*2, "<font style=\"background:yellow;\">")  
            wordList.insert(index + num*2+ len(keyword)+1, "</font>")      

        wordList = "".join(wordList)
        wordList = wordList.replace("\n","<br>")
        self.TextBrowser.setText(wordList)

    def ItemClicked(self):
        self.item_index = self.DoclistWidget.currentRow()
        self.TextBrowser.setText(self.contentList[self.itemList[self.item_index]])
        numList = self.Statistics[self.itemList[self.item_index]]
        self.Cal.setText('Number of characters:'+numList[0]+'\nNumber of words:'+numList[1]+'\nNumber of sentences:'+numList[2])
        self.FindClicked()

    def Read(self):
        self.TextBrowser.clear()
        self.DoclistWidget.clear()
        self.contentList.clear()

        if self.filename[0].endswith(".xml"):
            tree = ET.parse(f'{self.filename[0]}')
            root = tree.getroot()
            Article = root.findall("PubmedArticle")
            for elem in Article:
                doc = elem.find("MedlineCitation").find("Article")
                content = []
                content.append(doc.find("ArticleTitle").text+"\n\n")
                if doc.find("Abstract"):
                    content.append("Abstract\n\n")
                    abs = doc.find("Abstract").findall("AbstractText")
                    for part in abs:
                        if 'Label' in part.attrib:
                            content.append(part.attrib['Label']+":\n")
                        content.append(part.text+"\n\n")
                else:
                    content.append("No abstract available\n")
                content = "".join(content)
                num_char = str(len(content))
                num_word = str(len(content.split()))
                num_sentences = len(re.split(r'[.:?!]', content))
                if re.split(r'[.:]',content)[-1]== '\n\n':
                    num_sentences -= 1
                content = content.replace("<", "&lt;")
                content = content.replace(">", "&gt;")
                self.Statistics[doc.find("ArticleTitle").text] = [num_char, num_word, str(num_sentences)]
                self.contentList[doc.find("ArticleTitle").text] = content
        elif self.filename[0].endswith(".json"):
            content = []
            with open(f'{self.filename[0]}', 'rb')as fjson:
                twitter = json.load(fjson)
            for tweet in twitter:
                content.append(tweet["full_name"]+"@"+tweet["username"]+"\n"+tweet["tweet_text"]+"\n")
            content = "\n".join(content)
            num_char = str(len(content))
            num_word = str(len(content.split()))
            num_sentences = len(re.split(r'[.:?!]', content))
            if re.split(r'[.:]',content)[-1]== '\n\n':
                num_sentences -= 1
            content = content.replace("<", "&lt;")
            content = content.replace(">", "&gt;")
            self.Statistics["twitter"] = [num_char, num_word, str(num_sentences)]
            self.contentList["twitter"] = content

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
