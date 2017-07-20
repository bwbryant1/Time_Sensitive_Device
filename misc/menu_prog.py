from Tkinter import *


def doNothing():
    print "something"





root = Tk()
root.wm_title("Cyberstorm Bomb - Control Panel")
root.resizable(width=FALSE,height=FALSE)
root.minsize(width=650,height=350)

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu,tearoff=0)
editMenu = Menu(menu,tearoff=0)
viewMenu = Menu(menu,tearoff=0)
settingsMenu = Menu(menu,tearoff=0)
helpMenu = Menu(menu)


menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Edit",menu=editMenu)
menu.add_cascade(label="View",menu=viewMenu)
menu.add_cascade(label="Settings",menu=settingsMenu)
menu.add_command(label="Quit",command=root.quit)

fileMenu.add_command(label="New Project..",command=doNothing)

""" Login """

loginFrame = Frame(root)

label_user = Label(loginFrame,text="User: ")
label_pass = Label(loginFrame,text="Pass: ")
label_connected = Label(loginFrame,text="Disconected",bg="red")

user_box = Entry(loginFrame,width=50)
pass_box = Entry(loginFrame,show="*",width=50)

label_user.grid(row=0,column=0,sticky=W)
user_box.grid(row=0,column=1,sticky=E+W)

label_pass.grid(row=1,column=0,sticky=W)
pass_box.grid(row=1,column=1,sticky=E+W)

label_connected.grid(row=0,column=2,rowspan=2,sticky=N+S+E+W)

loginFrame.pack(fill=BOTH)



""" toolbar """

toolbar = Frame(root, bg="grey")
insertButton = Button(toolbar,text="Login",command=doNothing)

insertButton.pack(padx=2,pady=2,fill=X)
toolbar.pack(side=TOP,fill=X)

""" About """



""" Status Bar """
statusbar = Label(root, text="Preparing to do nothing",bd=1,relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)


root.mainloop()
