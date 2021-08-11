from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
root = Tk()
root.geometry("666x466")
root.title("Notepad")
img = PhotoImage(file="C:\\Users\\HP\\Downloads\\note.png")
root.iconphoto(False,img)
def new():
    global file
    root.title("Untitled_Note")
    file = None
    text.delete(1.0, END)#1.0 means from 1st line and 0th char se end tak sab data do

def Open():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                              ("Text Documnets", "*.txt")])
    if file == "": # if there is no file to open
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")# we will open file from the path defined
        text.delete(1.0, END)#Delete the current text
        f = open(file,'r')
        text.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file==None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                              ("Text Documnets", "*.txt")])
        if file=="":
            file=None
        else:
            # save as a new file
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File saved")

    else:
        # save the new file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()



def Exit():
    root.destroy()

def cut():
    text.event_generate(("<<Cut>>"))# Defined events

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("About notepad", "Notepad by Aayushi_07")

#Creating the menu bar
Mainmenu = Menu(root)
m1 = Menu(Mainmenu, tearoff=0)
m1.add_command(label="New", command=new)
#m1.add_command(label="New Window", command=newWindow)
m1.add_command(label="Open...", command=Open)
m1.add_command(label="Save", command=save)
m1.add_separator()
#m1.add_command(label="Save As", command=saveAs)
#m1.add_command(label="Page Setup", command=page)
#m1.add_command(label="Print..", command=Print)
m1.add_command(label="Exit", command=Exit)
Mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(Mainmenu, tearoff=0)
m2.add_command(label="Cut", command=cut)
m2.add_command(label="copy", command=copy)
m2.add_command(label="Paste", command=paste)
Mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(Mainmenu, tearoff=0)
m3.add_command(label="About Notepad", command=about)
Mainmenu.add_cascade(label="Help", menu=m3)

root.config(menu=Mainmenu)

# creating a text widget
text = Text(root)
file = None
text.pack(expand=True, fill=BOTH)
# creating a scroll bar
sc = Scrollbar(text)

sc.pack(side=RIGHT, fill=Y)

sc.config(command=text.yview)

text.config(yscrollcommand=sc.set)



root.mainloop()