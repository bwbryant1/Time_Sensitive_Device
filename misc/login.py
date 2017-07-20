from Tkinter import *
import sys,os

root = Tk()

def leftClick(event):
	print "left"

def rightClick(event):
	print "roght"
	#sys.exit()

def middleClick(event):
	print "middle"

subFrame = Frame(root,width=300,height=250)
subFrame.bind("<Button-1>",leftClick)
subFrame.bind("<Button-2>",middleClick)
subFrame.bind("<Button-3>",rightClick)

label_user = Label(root,text="User: ")
label_pass = Label(root,text="Pass: ")

user_box = Entry(root)
pass_box = Entry(root)

label_user.grid(row=0,column=0,sticky=W)
user_box.grid(row=0,column=1,sticky=W)

label_pass.grid(row=1,column=0,sticky=W)
pass_box.grid(row=1,column=1,sticky=W)

c = Checkbutton(root,text="Keep alive")
c.grid(row=3,column=0,columnspan=2)

#subFrame.grid(row=4)
root.mainloop()
