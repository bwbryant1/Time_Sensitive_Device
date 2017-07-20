from Tkinter import *
from PIL import ImageTk, Image
class Counter(object):

    def __init__(self, time, frame):
        self.armed = 1
        self.start_time = time
        self.frm = frame

        self.counter = self.start_time
        self.curr_epoch = 0 
        self.start_epoch = 0
        

        self.label = frame.create_text(151, 285, text="", fill="white",font=('Helvetica', 20,'bold'),justify=CENTER,anchor=CENTER,width=300)
        self.label_inner = frame.create_text(150, 285, text="", fill="black",font=('Helvetica', 20,'bold'),justify=CENTER,anchor=CENTER,width=300)        

    def decrement(self, x):
        if self.start_time - (self.curr_epoch - self.start_epoch) > 0:
            self.counter = self.start_time - (self.curr_epoch - self.start_epoch)
            
        else:
            self.counter = 0
            self.armed = 2
            
    def set_time(self,x):
        self.frm.itemconfig(self.label,text=x)
        self.frm.itemconfig(self.label_inner,text=x)

    def set_curr_epoch(self,y,x,z):
        self.curr_epoch = x
        self.start_epoch = y
        self.armed = z
       
        #print self.curr_epoch - self.start_epoch

class Score(object):
    def __init__(self,team_name,score, frame,img):

        self.frm = frame

        image = Image.open("img/"+img)
        image = image.resize((250, 250), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(image)
        self.frm.create_image(150, 150, image=self.photoimage)

        self.label_team = frame.create_text(152, 20, text=team_name, fill="#000",font=('Helvetica', 20,'bold'),justify=CENTER,anchor=CENTER,width=300)
        
        self.label_team_inner = frame.create_text(150, 20, text=team_name, fill="#FFF",font=('Helvetica', 20,'bold'),justify=CENTER,anchor=CENTER,width=300)        
        
        
        self.label = frame.create_text(152, 150, text=str(score), fill="#000",font=('Helvetica', 48,'bold'),justify=CENTER,anchor=CENTER,width=300)
        
        self.label_inner = frame.create_text(150, 150, text=str(score), fill="#FFF",font=('Helvetica', 48,'bold'),justify=CENTER,anchor=CENTER,width=300)
                
        
    def set_score(self,x):
        self.frm.itemconfig(self.label,text=x)
        self.frm.itemconfig(self.label_inner,text=x)

