from tkinter import *
from tkinter.filedialog import asksaveasfile
from keyboard import add_hotkey
from tkinter import filedialog as fd
from tkinter import messagebox


#commands
commslist = ['write@new^^ ', 'write^^ ', 'numerous ', 'string ', 'list ', 'bool', 'times$do% ', 'take$v}', 'in@']
#is do
isdo = '& '
#is take on new string or not
istakenew = '< '
#should write list
shouldwrite = []
#taked by take$
taked = {}
#comms should do
commsdo = 1
#strings are
strsgrid = 1
#run all time
runtime = 0
strings_grides = []
#debug
sc = False
#clear log
cl = False
#strings in debug window
debug_strings = 1
#if correct include, print error on take NONE
t_in_e = True


def change_uc_var_i():
    global t_in_e
    if t_in_e:
        t_in_e = False
    else:
        t_in_e = True


def clear_log():
    global cl
    if cl:
        cl = False
    else:
        cl = True


def show_inside_comms():
    global sc, debug_win
    sc = True
    debug_win = Tk()
    debug_win.title('Debuger')
    debug_win.geometry('1024x512')
    debug_win.mainloop()
    


def save_file():
    try:
         with asksaveasfile(initialfile = 'Project.Macinton', defaultextension="",filetypes=[("All Files","*.*"),("Macinton","*Macinton")]) as f:
              for entry in comms:
                   f.write(entry.get()+'\n')
    except:
        pass


def open_helper():
     messagebox.showinfo(title='Helper', message='ctrl + s: save file \nctrl + o: open file(open only in studio!) \nctrl + h: open helper \nctrl + r: run code\nctrl + tab + c: clear logs(run to clear)\nctrl + d: show debuger\nMacinton\ndtudio 1.0 by Ivan Lyalchenko 2023 ')
    
    
def run_code():
    global comms, commsdo, shouldwrite, strsgrid, runtime, string, sc, debug_win, cl, strings_grides, debug_strings, t_in_e
    #list with commands
    takelist = []
    for comlist in comms:
          takelist.append(comlist.get())
          commsdo += 1
          
    #print(comms)
    for takecom in takelist:
        if sc:
            debug_string = Label(debug_win ,text=takecom)
            debug_string.grid(column=1, row=debug_strings)
            debug_strings += 1
        if takecom[0:14] == isdo + commslist[0]:
              string = Label(text=takecom[14:])
              strings_grides.append(string)
              if cl == False:
                    string.grid(column=200, row=strsgrid)
                    strsgrid += 1
              #clear logs
              if cl:
                  for take_string in strings_grides:
                    take_string.destroy()

                  cl = False
                  strsgrid = 1
        elif takecom == '%var_error_be%':
            change_uc_var_i()

        elif 'take$' in takecom:
            print('num')
            new_str = takecom[0:4] == '& < '
            var_type = ''
            if new_str:
                #var type(nemurous, string, list, bool)
                var_type = takecom[4:takecom.index('$')-5]
                print(var_type)
                #var name take$VAR NAME}VAR INCLUDES(if nothing or ucorrect include var includes, var includes NONE. NONE + int = int, NONE + string = string)
                var_name = takecom[4+len(var_type)+6:takecom.index('}')]
                print(var_name)
                if var_type == 'numerous':
                    for char_take_var_check in takecom[4+8+5+len(var_name)+1]:
                        #check correct
                        if char_take_var_check is not [str(i) for i in range(11)]:
                            #is uncorrect could be
                            if t_in_e:
                                include_var_none = [var_type, 'NONE']
                                taked[var_name] = include_var_none
                                print(taked.get(var_name[1]))
                            else:
                                messagebox.showinfo(title='Var error', message='Var error. Solves: change include or use &var_error_be')
                                break



    runtime += 1

        
strscode = 1
stringsare = 1
opened = 0
def open_file():
    try:
         global opened, strscode, stringsare, runtime
         opened = 1
         with fd.askopenfile(mode='r') as reader:
              global commas
              commas = reader.readlines()
              commasw = 1
              for commasnames in commas:
                   newenter = Entry(windo, width=128)
                   newenter.grid(column=1, row=commasw)
                   newenter.insert(0, commasnames.strip())
                   newenter.bind('<Return>', newtake)
                   commasw += 1
              strscode = commasw
              stringsare = strscode
              runtime = 0
         return opened, strscode, stringsare
    except:
         pass
         
        
takenew = 1
comms = []


def newtake(event):
     global strscode, stringsare, windo, newenter, takenew
     if strscode == 1:
          comms.append(newenter)
     newenter = Entry(windo, width=128)
     newenter.grid(column=1, row=stringsare+1)
     comms.append(newenter)
     stringsare += 1
     strscode += 1
     newenter.bind('<Return>', newtake)
     return stringsare, strscode


windo = Tk()
windo.title('Macinton')
windo.geometry('2048x1024')


help = Button(windo, text='Open helper', command=open_helper)
help.grid(column=10, row=1)


run = Button(windo, text='RUN', command=run_code)
run.grid(column=11, row=1)


safe = Button(windo, text='Safe file', command=save_file)
safe.grid(column=12, row=1)


open_button = Button(windo, text='Open file', command=open_file)
open_button.grid(column=13, row=1)


#hotkeys
add_hotkey('ctrl + h', open_helper, args=())
add_hotkey('ctrl + s', save_file, args=())
add_hotkey('ctrl + o', open_file, args=())
add_hotkey('ctrl + r', run_code, args=())
add_hotkey('ctrl + d', show_inside_comms, args=())
add_hotkey('ctrl + tab + c', clear_log, args=())


#main window
newenter = Entry(windo, width=128)
newenter.grid(column=1, row=stringsare)
newenter.bind("<Return>", newtake)
windo.mainloop()