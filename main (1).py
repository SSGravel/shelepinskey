from random import choise,shuffle
from PyQt5.QtWidgets import QApplication

app = QApplication([])








class Question:
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def gor_wrong(self):
        self.count_ask += 1



q1 = Question('Яблоко','apple','application','pinapple','apply')
q2 = Question('Дім','house','horse','amought','hour')
q3 = Question('Миша','mouse','mouth','muse','museum')
q4 = Question('ЧИсло','number','digit','amount','summary')


radio_buttons = [rb_ans1,rb_ans2,rb_ans3,rb_ans4]