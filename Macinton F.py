from tkinter import *
from tkinter.filedialog import asksaveasfile
from keyboard import add_hotkey
from tkinter import filedialog as fd
from tkinter import messagebox
from webbrowser import *


#commands
commslist = ['write@new^^ ', 'write^^ ', 'numerous ', 'string ', 'list ', 'bool', 'times$do% ', 'take$v}', 'in@']
#is do
isdo = '& '

#should write list
shouldwrite = []
#let's do vars for vars
vars_names = []
vars_include = []
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
#takelist
takelist = []
#comms
comms = []
#logs list
logs = []
#settings
sb = False
#find vars in write
vars_collected = []


def check_include(find_in, your_list):
    before = 0
    for take in your_list:
        if take in find_in:
            your_list.append(take)
            before += 1


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
         with asksaveasfile(initialfile = 'Project.', defaultextension="",filetypes=[("All Files","*.*"),("Macinton","*mcfp")]) as f:
              for entry in comms:
                   f.write(entry.get()+'\n')
    except:
        pass


def open_helper():
     messagebox.showinfo(title='Helper', message='ctrl + s: save file \nctrl + o: open file(open only in studio!) \nctrl + h: open helper \nctrl + r: run code\nctrl + tab + c: clear logs(run to clear)\nctrl + d: show debuger\nMacinton\ndtudio 1.0 by Ivan Lyalchenko 2023 ')
    
    
def run_code():
    global comms, commsdo, shouldwrite, strsgrid, runtime, string, sc, debug_win, cl, strings_grides, debug_strings, t_in_e, takelist, logs, sb, vars_include, vars_names
    #list with commands
    takelist = []
    for comlist in comms:
          takelist.append(comlist.get())
          commsdo += 1
          
    #print(comms)
    for takecom in takelist:
        if sc:
            try:
                debug_string = Label(debug_win ,text=takecom)
                debug_string.grid(column=1, row=debug_strings)
                debug_strings += 1
            except:
                pass

        if takecom[0:14] == isdo + commslist[0]:
              if vars_names:
                  string = Label(text=takecom[14:])
                  strings_grides.append(string)

              else:
                  string = Label(text=vars_include[vars_names.index(takecom[14:])])
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

        elif takecom == '#PROJECT SETTINGS#':
            if sb == False:
                sb = True
            else:
                sb = False


        elif takecom == '%var_error_be%' and sb:
            change_uc_var_i()

        elif takecom == '%chat%' and sb:
            open_new('https://t.me/+fd3TDUusml9iNzhi')

        elif takecom == '%hbf!%':
            messagebox.showinfo(title='Happy Birthday!', message='Happy Birthday!')

        elif 'take$' in takecom:
            print('num')
            new_str = takecom[0:4] == '& < '
            var_type = ''
            if new_str:
                #var type(numerous, string, list, bool)
                var_type = takecom[4+takecom.index('$'):]
                print(var_type)
                #var name take$VAR TYPE$VAR NAME}VAR INCLUDESif nothing or ucorrect include var include, var includes NONE. NONE + numerous = numerous, NONE + string = string)
                #do var name
                var_name = takecom[4+len(var_type)+1:]
                finish_index = var_name.index('$')
                var_name = var_name[finish_index:]
                print(var_name)
                var = takecom[4+8+5+len(var_name)+2:]
                if var_type == 'numerous':
                    for char_take_var_check in takecom[4+8+5+len(var_name)+2:]:
                        #check correct
                        print(char_take_var_check)
                        if char_take_var_check is not ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '-']:
                            #is uncorrect could be
                            if t_in_e or var.count(',') > 1 or var.count('.') > 1 or var.count('-') > 1:
                                include_var_none = [var_type, 'NONE']
                                vars_names.append(var_name)
                                vars_include(var)
                            else:
                                messagebox.showinfo(title='Var error', message='Var error. Solves: change include or use &var_error_be%')
                                break


    runtime += 1

comms.clear()
     
strscode = 1
stringsare = 1
opened = 0
def open_file():
    try:
         global opened, strscode, stringsare, runtime
         opened = 1
         with fd.askopenfile(mode='r', filetypes=[('Macinton', '*mcfp')]) as reader:
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
try:
    windo.iconbitmap('nsr.ico')
except:
    messagebox.showerror(title='File error', message='Icon has been removed. Back icon to the dir with Macinton\nUnless delete and install Macinton again')
    exit()


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