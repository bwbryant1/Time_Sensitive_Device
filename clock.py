#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkinter import *
import time, sys
from PIL import ImageTk, Image
from classes import Counter, Score
import MySQLdb as mdb

w = 1200  # width for the Tk root
h = 600  # height for the Tk root
    
def Create_Teams(self):

    self.teamOneFrame = Canvas(self, bg='#cc0', width=w/4, height=h/2,highlightthicknes=1)
    self.teamOneFrame.grid(row=0, column=0)

    self.teamTwoFrame = Canvas(self, bg='#00a', width=w/4, height=h/2,highlightthicknes=1)
    self.teamTwoFrame.grid(row=0, column=1)

    self.teamThreeFrame = Canvas(self, bg='#0bb', width=w/4, height=h/2,highlightthicknes=1)
    self.teamThreeFrame.grid(row=0, column=2)

    self.teamFourFrame = Canvas(self, bg='#CF5300', width=w/4, height=h/2,highlightthicknes=1)
    self.teamFourFrame.grid(row=0, column=3)
    
    self.teamFiveFrame = Canvas(self, bg='#FFBAD2', width=w/4, height=h/2,highlightthicknes=1)
    self.teamFiveFrame.grid(row=1, column=0)

    self.teamSixFrame = Canvas(self, bg='grey', width=w/4, height=h/2,highlightthicknes=1)
    self.teamSixFrame.grid(row=1, column=1)

    self.teamSevenFrame = Canvas(self, bg='#b00', width=w/4, height=h/2,highlightthicknes=1)
    self.teamSevenFrame.grid(row=1, column=2)

    self.teamEightFrame = Canvas(self, bg='#0b0', width=w/4, height=h/2,highlightthicknes=1)
    self.teamEightFrame.grid(row=1, column=3)



def __setup__(self):
    
    self.con = mdb.connect('localhost', 'testuser', 'test623', 'bomb');    
    
    self.wm_title('Cyberstorm Bomb - Countdown Screen')

    w = 1200  # width for the Tk root
    h = 600  # height for the Tk root

    ws = self.winfo_screenwidth()  # width of the screen
    hs = self.winfo_screenheight()  # height of the screen

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    self.minsize(width=w, height=h)
    #self.attributes("-fullscreen", True)
    self.resizable(width=tk.FALSE, height=tk.FALSE)
    self.running = False
    self.run_once = True


def Quit(self):

    sys.exit()


def formatTime(x):
    m, s = divmod(x, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


class CountdownScreen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        __setup__(self)
        
        Create_Teams(self)

        self.scores = [
            Score("Bowser",5, self.teamOneFrame,"Bowser2.png"),
            Score("Conker",1800, self.teamTwoFrame,"conker.png"),
            Score("Funky Kong",3600 * 4, self.teamThreeFrame,"funky.png"),
            Score("Glados",3600 * 4, self.teamFourFrame,"glados.png"),
            Score("Kirby",3600 * 3, self.teamFiveFrame,"kirby.png"),
            Score("R.O.B.",3600 * 3, self.teamSixFrame,"rob.png"),
            Score("Shadow",3600 * 2, self.teamSevenFrame,"shadow.png"),
            Score("Shodan",3600 * 2, self.teamEightFrame,"shodan.png"),

        ]

        self.counters = [
            Counter(3600*2, self.teamOneFrame),
            Counter(3600*2, self.teamTwoFrame),
            Counter(3600*2, self.teamThreeFrame),
            Counter(3600*2, self.teamFourFrame),
            Counter(3600*2, self.teamFiveFrame),
            Counter(3600*2, self.teamSixFrame),
            Counter(3600*2, self.teamSevenFrame),
            Counter(3600*2, self.teamEightFrame),
            ]


        self.update_all()

    def update_counters(self):
        curr_epoch = int(time.time())
        
        for obj in self.counters:
            if obj.armed == 1:
                now = formatTime(obj.counter) + ' - ARMED'
                obj.set_time(now)
                obj.decrement(1)
            elif obj.armed == 0:
                now = formatTime(obj.counter) + ' - DISARMED'
                obj.set_time(now)

            else:
                now = formatTime(obj.counter) + ' - BLOWN'
                obj.set_time(now)
            
    def update_score(self):
        curr_epoch_1 = int(time.time())
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM Teams")

            for i in xrange(cur.rowcount):
                
                row = cur.fetchone()
                self.scores[i].set_score(row[2])
                self.counters[i].set_curr_epoch(row[3],curr_epoch_1,row[4])
                #print self.counters[i].curr_epoch


    def update_running(self):
        f = open("running")
        b = f.read()
        if b == "run":
            self.running = True
            #print "running"
        else:
            self.running = False
            #print "not running"

        f.close()
    
    def update_all(self):
        self.update_running()
        if self.running:
            self.update_counters()
            self.update_score()

        self.after(1000, self.update_all)

if __name__ == '__main__':
    app = CountdownScreen()
    try:
        app.mainloop()
    except:
        print "\nDone"

