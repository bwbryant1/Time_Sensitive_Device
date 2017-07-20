#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkinter import *
import time


def Create_Teams(self):
    self.teamOneFrame = Frame(self, bg="black", width=300, height=300)
    self.teamOneFrame.grid(row=0, column=0)
    self.teamOneFrame.grid_propagate(False)

    self.teamTwoFrame = Frame(self, bg="red", width=300, height=300)
    self.teamTwoFrame.grid(row=0, column=1)

    self.teamThreeFrame = Frame(self, bg="blue", width=300, height=300)
    self.teamThreeFrame.grid(row=0, column=2)

    self.teamFourFrame = Frame(self, bg="green", width=300, height=300)
    self.teamFourFrame.grid(row=0, column=3)

    self.teamFiveFrame = Frame(self, bg="grey", width=300, height=300)
    self.teamFiveFrame.grid(row=1, column=0)

    self.teamSixFrame = Frame(self, bg="magenta", width=300, height=300)
    self.teamSixFrame.grid(row=1, column=1)

    self.teamSevenFrame = Frame(self, bg="pink", width=300, height=300)
    self.teamSevenFrame.grid(row=1, column=2)

    self.teamEightFrame = Frame(self, bg="yellow", width=300, height=300)
    self.teamEightFrame.grid(row=1, column=3)


ran = False

class CountdownScreen(tk.Tk):




    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title('Cyberstorm Bomb - Countdown Screen')
        # self.attributes("-fullscreen", True)
        self.resizable(width=tk.FALSE, height=tk.FALSE)
        self.minsize(width=1200, height=600)


        Create_Teams(self)


        team1 = Label(self.teamOneFrame,text="Hello")
        team1.pack(side=LEFT,expand=0)


        self.update_all()


    def update_clock(self):
        now = time.strftime('%H:%M:%S', time.gmtime())
        # self.counter.configure(text=now)

    def update_all(self):
        self.update_clock()
        self.after(1000, self.update_all)


if __name__ == '__main__':
    app = CountdownScreen()
    app.mainloop()

