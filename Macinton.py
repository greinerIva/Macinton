from tkinter import *
from tkinter.filedialog import asksaveasfile
from keyboard import add_hotkey
from tkinter import filedialog as fd


def save_file():
    with asksaveasfile(initialfile = 'Untiled.macinton0', defaultextension=".macinton0",filetypes=[("All Files","*.*"),("Macinton 0","*.macinton0")]) as f:
        for entry in comms:
            f.write(entry.get()+'\n')
        

opened = 0
def open_file():
    global opened
    opened = 1
    with fd.askopenfile(mode='r') as reader:
        commas = reader.readlines()
        commasw = 1
        for commasnames in commas:
            newenter = Entry(windo, width=128)
            newenter.grid(column=1, row=commasw)
            newenter.insert(0, commasnames)
            newenter.bind('<Return>', newtake)
            commasw += 1
        strscode = commasw
    return opened, strscode
        
        

comms = []
if opened != 1:
    strscode = 1

def newtake(event):
    global strscode, stringsare, windo, newenter
    if strscode == 1:
        #comms.append(newenter.get())
        comms.append(newenter)
    newenter = Entry(windo, width=128)
    newenter.grid(column=1, row=stringsare+1)
    comms.append(newenter)
    stringsare += 1
    strscode += 1
    newenter.bind('<Return>', newtake)
    return stringsare, strscode

if opened != 1:
    stringsare = 1

windo = Tk()
windo.title('Macinton 0')
windo.geometry('2048x1024')

add_hotkey('ctrl + s', save_file, args=())
add_hotkey('ctrl + o', open_file, args=())


newenter = Entry(windo, width=128)
newenter.grid(column=1, row=stringsare)
newenter.bind("<Return>", newtake)
windo.mainloop()