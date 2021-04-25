import os
import sys
import time
import random
import tkinter
import tkinter.font
from tkinter import Tk
from tkinter import ttk

class Q:
    def __init__(self, file="data.txt"):
        self.__q = ""
        self.__a = ""
        self.table = self.open_list(file)
        self.question = tkinter.StringVar()
        self.result = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.answer = tkinter.StringVar()
        self.number = 0
        self.total = 20
        self.misstakes = 0
    @property
    def q(self):
        return self.__q
    @q.setter
    def q(self, v):
        self.__q = v
        
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, v):
        self.__a = v

    def open_list(self, file):
        table = {}
        with open(file) as f:
            data = f.readlines()
            entries = [d.split(",") for d in data]
            for entry in entries:
                table[entry[1].strip()] = entry[0].strip()
        return table

    def get_question(self):
        i = random.randrange(len(self.table))
        return list(self.table.items())[i]

    def check_answer(self):
        print("yours", q.answer.get())
        flag = (q.answer.get() == self.a)
        print(flag)
        if(flag):
            self.result.set('OK!!')
            if(self.total == self.number):
                sys.exit()
            self.make_next_question()
        else:
            self.result.set('Error!!')
            self.misstakes = self.misstakes + 1
        self.answer.set('')
        self.status.set(str(self.number) + '/' + str(self.total) + ' (miss.=' + str(self.misstakes) + ')')
        return flag

    def make_next_question(self):
        self.number = self.number + 1
        self.status.set(str(self.number) + '/' + str(self.total) + ' (miss.=' + str(self.misstakes) + ')')
        ret = self.get_question()
        self.q = ret[0]
        self.a = ret[1]
        self.question.set(q.q)

root = Tk()
root.title('Word Practice')
root.resizable(False, False)

q = Q(file=os.environ["HOME"]+"/data.txt")

frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

font = tkinter.font.Font(weight="bold", size=20)

label0 = ttk.Label(frame1, text='Try!', padding=(5, 2), font=font)
label0.grid(row=0, column=0, sticky=tkinter.W)

label1 = ttk.Label(frame1, text='Answer', padding=(5, 2), font=font)
label1.grid(row=1, column=0, sticky=tkinter.W)

question_label = ttk.Label(frame1, textvariable=q.question, width=20, font=font)
question_label.grid(row=0, column=1, sticky=tkinter.W)
q.make_next_question()

answer_label = ttk.Entry(frame1, textvariable=q.answer, width=20, font=font)
answer_label.grid(row=1, column=1)
answer_label.bind("<Return>", lambda event:q.check_answer())

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=3, column=1, sticky=tkinter.W)

result_label = ttk.Label(frame1, textvariable=q.result, width=20, font=font)
result_label.grid(row=4, column=0)

status_label = ttk.Label(frame1, textvariable=q.status, width=20, font=font)
status_label.grid(row=4, column=1)

button1 = ttk.Button(
    frame2, text='OK',
    command=lambda: q.check_answer())
button1.pack(side=tkinter.LEFT)

root.mainloop()
