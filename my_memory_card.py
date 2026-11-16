#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, 
    QGroupBox, QPushButton, QButtonGroup
)
from random import shuffle, randint
 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def next_question():
    main_win.total += 1
    print('Статистика')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)
    current = randint(0, len(question_list) - 1)
    ask(question_list[current])

def show_result():
    group_visual.hide()
    group_visual_res.show()
    btn.setText('Следующий вопрос')

def show_question():
    group_visual.show()
    group_visual_res.hide()
    btn.setText('Ответить')
    logic_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    logic_group.setExclusive(True)

def ask(q: Question):
    shuffle(radio_list)
    radio_list[0].setText(q.right_answer)
    radio_list[1].setText(q.wrong1)
    radio_list[2].setText(q.wrong2)
    radio_list[3].setText(q.wrong3)
    lb_title.setText(q.question)
    lb_res_bottom.setText(q.right_answer)
    show_question()

def check_answer():
    if radio_list[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if radio_list[1].isChecked() or radio_list[2].isChecked() or radio_list[3].isChecked():
            show_correct('Неправильно!')
        print('Рейтинг:', str(round(main_win.score/main_win.total*100, 1)) + '%')

def show_correct(res):
    lb_res_top.setText(res)
    show_result()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')
btn = QPushButton('Ответить')
lb_title = QLabel('Какой национальности не существует?')
group_visual = QGroupBox('Варианты ответов')
group_visual_res = QGroupBox('Результат теста')
lb_res_top = QLabel('Правильно/Неправильно')
lb_res_bottom = QLabel('Правильный ответ')

logic_group = QButtonGroup()
logic_group.addButton(rbtn1)
logic_group.addButton(rbtn2)
logic_group.addButton(rbtn3)
logic_group.addButton(rbtn4)

lv_ans_left = QVBoxLayout()
lv_ans_left.addWidget(rbtn1)
lv_ans_left.addWidget(rbtn3)

lv_ans_right = QVBoxLayout()
lv_ans_right.addWidget(rbtn2)
lv_ans_right.addWidget(rbtn4)

lh_ans_group = QHBoxLayout()
lh_ans_group.addLayout(lv_ans_left)
lh_ans_group.addLayout(lv_ans_right)

lv_res_group = QVBoxLayout()
lv_res_group.addWidget(lb_res_top)
lv_res_group.addWidget(lb_res_bottom, alignment = Qt.AlignCenter)

group_visual_res.setLayout(lv_res_group)

group_visual.setLayout(lh_ans_group)

lv_main = QVBoxLayout()
lv_main.addWidget(lb_title, alignment = Qt.AlignCenter)
lv_main.addWidget(group_visual)
lv_main.addWidget(group_visual_res)
group_visual_res.hide()
lv_main.addWidget(btn)

main_win.setLayout(lv_main)

radio_list = [rbtn1, rbtn2, rbtn3, rbtn4]

question_list = []
question_list.append(Question('Какого цвета нету в флаге Российской империи?', 'Синий', 'Желтый', 'Черный', 'Белый'))
question_list.append(Question('В каком году казнили Карла 1?', '1649 год', '1647 год', '1643 год', '1648 год'))
question_list.append(Question('Сколько штатов в США?', '51', '46', '63', '56'))
question_list.append(Question('Сколько хромосом у Ивана Золо?', '47', '45', '48', '2'))

btn.clicked.connect(click_OK)

main_win.total = 0
main_win.score = 0

next_question()

main_win.show()
app.exec_()