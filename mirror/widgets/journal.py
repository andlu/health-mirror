from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from mirror.widgets.listener import record_and_parse_audio

class Journal(QWidget):
    journal_entries = []

    def __init__(self, parent):
        super(Journal, self).__init__()
        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: white;')
        self.wordLabel.setGeometry(50, 50, 500, 200)
    
    def doJournal(self):
        numbers = ["first", "second", "third"]
        for number in numbers:
            question = ("Say the {} thing you are grateful for".format(number))
            self.wordLabel.setText(question)
            self.wordLabel.repaint()
            word_string = record_and_parse_audio()
            self.journal_entries.append(word_string)
        
        output = "I am grateful for:\n"
        output += "1) " + self.journal_entries[-3] + "\n"
        output += "2) " + self.journal_entries[-2] + "\n"
        output += "3) " + self.journal_entries[-1] + "\n"
        self.wordLabel.setText(output)
    
    def readEntries(self):
        if (len(self.journal_entries) < 3):
            return
        
        output = "1) " + self.journal_entries[-3] + "\n"
        output += "2) " + self.journal_entries[-2] + "\n"
        output += "3) " + self.journal_entries[-1] + "\n"
        self.wordLabel.setText(output)

    def show(self):
        self.wordLabel.show()
    
    def hide(self):
        self.wordLabel.hide()