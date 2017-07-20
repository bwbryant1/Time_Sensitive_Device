from Tkinter import *
import sys, os

def left():
    os.system("curl http://138.47.54.245/cgi-bin/viewer/camctrl.cgi?move=left")
def right():
    os.system("curl http://138.47.54.245/cgi-bin/viewer/camctrl.cgi?move=right")
def up():
    os.system("curl http://138.47.54.245/cgi-bin/viewer/camctrl.cgi?move=up")
def down():
    os.system("curl http://138.47.54.245/cgi-bin/viewer/camctrl.cgi?move=down")

root = Tk()

leftBtn = Button(root,text="left",command=left)
rightBtn = Button(root,text="right",command=right)
upBtn = Button(root,text="up",command=up)
downBtn = Button(root,text="down",command=down)

upBtn.grid(row=0,columnspan=4)
leftBtn.grid(row=1)
rightBtn.grid(row=1,column=3)
downBtn.grid(row=2,columnspan=4)


root.mainloop()
