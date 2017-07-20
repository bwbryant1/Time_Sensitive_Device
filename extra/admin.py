#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkinter import *
import time
import socket
from hashlib import sha256 
import ssl





class AdminPanel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title('Cyberstorm Bomb - Control Panel')

        self.resizable(width=tk.FALSE, height=tk.FALSE)
        self.minsize(width=650, height=350)

        menu = Menu(self)
        self.config(menu=menu)
	
        fileMenu = Menu(menu, tearoff=0)
        editMenu = Menu(menu, tearoff=0)
        viewMenu = Menu(menu, tearoff=0)
        settingsMenu = Menu(menu, tearoff=0)
        helpMenu = Menu(menu)

        menu.add_cascade(label='File', menu=fileMenu)
        menu.add_cascade(label='Edit', menu=editMenu)
        menu.add_cascade(label='View', menu=viewMenu)
        menu.add_cascade(label='Settings', menu=settingsMenu)
        menu.add_command(label='Quit', command=self.quit)

        fileMenu.add_command(label='New Project..')

        loginFrame = Frame(self)

        label_user = Label(loginFrame, text='User: ')
        label_pass = Label(loginFrame, text='Pass: ')
	label_key = Label(loginFrame, text='Key: ')
        self.label_connected = Label(loginFrame, text='Disconected', bg='red'
                                )

        self.user_box = Entry(loginFrame, width=50)
        self.pass_box = Entry(loginFrame, show='*', width=50)
	self.key_box = Entry(loginFrame, show='*', width=50)

        label_user.grid(row=0, column=0, sticky=W)
        self.user_box.grid(row=0, column=1, sticky=E + W)

        label_pass.grid(row=1, column=0, sticky=W)
        self.pass_box.grid(row=1, column=1, sticky=E + W)

        label_key.grid(row=2, column=0, sticky=W)
        self.key_box.grid(row=2, column=1, sticky=E + W)

        self.label_connected.grid(row=0, column=2, rowspan=3, sticky=N + S
                             + E + W)

        loginFrame.pack(fill=BOTH)

        toolbar = Frame(self, bg='grey')
        insertButton = Button(toolbar, text='Login')
	insertButton.bind("<Button-1>",self.login)

        insertButton.pack(padx=2, pady=2, fill=X)
        toolbar.pack(side=TOP, fill=X)
	
	self.response = ""

        self.statusbar = Label(self, text='', bd=1,
                          relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)

        self.update_all()
	
    
    def update_disconnect(self):
	user = self.user_box.get()
	if self.response == "authenticated":
		self.label_connected.configure(text="sent",bg="green")
	else:
		self.label_connected.configure(text="not sent",bg="red")
	
    def update_clock(self):
        now = time.strftime('%H:%M:%S', time.gmtime())
        self.statusbar.configure(text=now)
	
    def update_all(self):
        self.update_clock()
        self.update_disconnect()
	self.after(1000, self.update_all)
   
    def login(self,event):
	self.label_connected.configure(text="waiting",bg="yellow")
	#self.response = ""
	user = self.user_box.get()
	passwd = self.pass_box.get()
	passwd = passwd + self.key_box.get()
	hashpass = sha256(passwd)
	
	

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', 8887))   
	sslSocket = socket.ssl(s)	
	
	sslSocket.write(user+":"+hashpass.hexdigest())
	self.response = sslSocket.read(65535)
	print self.response  
	s.close()  
	
	


if __name__ == '__main__':
    app = AdminPanel()
    app.mainloop()

			
