from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *

def hello():
    print("Hello!")



main_window = Tk()
title = "Paper"
saved_file = False
saved_filename = ""
current_file = ""
aboutMessage = "Paper 0.1 - Janurary 15, 2018\nCreated on Python 3.6.4 with Tkinter \n\n(C) lapisZ 2018\n"
window = None

main_window.title(title)
menubar = Menu(main_window)
main_window.iconbitmap("paper_icon.ico")
main_window.resizable(0, 0)

main_window.config(menu=menubar)
main_window.update()

tbox = ScrolledText(main_window)
tbox.grid(row=0)

def getFileNameFromPath(fullFileName):
    filenamereverse = ""
    filename = ""
    for index in range(-1, (-1 * len(fullFileName)) - 1, -1):
        if fullFileName[index] == "/":
            break
        else:
            filenamereverse = filenamereverse + fullFileName[index]

    for index in range(-1, (-1 * len(filenamereverse)) - 1, -1):
        filename = filename + filenamereverse[index]
        
    return filename
#########################
def openfile():
    global current_file
    global saved_file
    filename = ""
    fullfilename = askopenfilename(filetypes = (("Text Documents", "*.txt"), ("All Files", "*.*")))    
    if fullfilename == "" or fullfilename == None:
        return None        
    filecontents = open(fullfilename).read()
    tbox.delete(1.0, END)
    tbox.insert(INSERT, filecontents)

    filename = getFileNameFromPath(fullfilename)
        
    title = "Paper - " + filename
    main_window.title(title)
    current_file = fullfilename
    saved_file = True
##########################
def save():
    global saved_file
    if saved_file != True:
        saveas()
        return None
    file = open(current_file, "w")
    file.write(tbox.get("1.0", END))
    file.close()    
    saved_file = True
    
##########################
def saveas():
    global saved_file
    global current_file
    fullfilename = asksaveasfilename(defaultextension=".txt", filetypes=(("Text Documents", "*.txt"), ("All Files", "*.*")))
    if fullfilename == "" or fullfilename == None:
        return None
    
    file = open(fullfilename, "w")
    file.write(tbox.get("1.0", END))
    file.close()
    saved_file = True
    print(saved_file)
    filename = getFileNameFromPath(fullfilename)
    
    title = "Paper - " + filename
    main_window.title(title)
    current_file = fullfilename
###########################
def undo():
    global tbox
    try:
        tbox.edit_undo()
    except TclError:
        print("")
##############################
def redo():
    global tbox
    try:
        tbox.edit_redo()
    except TclError:
        print("")
#####################
def copyToCB():
    global tbox
    global main_window
    main_window.clipboard_clear()
    main_window.clipboard_append(tbox.selection_get())
###########################
def pasteFromCB():
    global tbox
    global main_window
    tbox.insert(INSERT, main_window.clipboard_get())
######################
def cutToCB():
    global tbox
    global main_window
    main_window.clipboard_clear()
    main_window.clipboard_append(tbox.selection_get())
    tbox.delete("sel.first", "sel.last")
######################
def selAll():
    global tbox
    tbox.tag_add(SEL, "1.0", END)
    tbox.focus_set()
########################
def destroyAboutLink(arg1):
    global window
    window.destroy()
    
#################
def aboutWindow():
    global aboutMessage
    global main_window
    global window
    
    window = Toplevel(main_window, width=300, height=100)
    window.title("About Paper")
    window.resizable(0, 0)
    window.grab_set()
    window.geometry("+%d+%d" % (main_window.winfo_rootx()+150, main_window.winfo_rooty()+80))

    message = Message(window, text=aboutMessage)
    message.grid(row=1, padx=80, pady=6)
    
    okay = Button(window, text="OK", command=window.destroy, width=10, height=1, pady=2)
    okay.grid(row=2)
    window.transient(main_window)
    window.focus_force()
    

    window.bind_all("<Return>", destroyAboutLink)
    window.bind_all("<Cancel>", destroyAboutLink)
    window.bind_all("<space>", destroyAboutLink)
    window.bind_all("<Escape>", destroyAboutLink)
    
##########
def openfile_link(event):
    openfile()

def save_link(event):
    save()

def saveas_link(event):
    saveas()

def exitfunc(event):
    exit()

############################
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open...", command=openfile, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=save, accelerator="Ctrl+S")
filemenu.add_command(label="Save As...", command=saveas)
filemenu.add_command(label="Exit", command=main_window.quit, accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", command=redo, accelerator="Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cutToCB, accelerator="Ctrl+X")
editmenu.add_command(label="Copy", command=copyToCB, accelerator="Ctrl+C")
editmenu.add_command(label="Paste", command=pasteFromCB, accelerator="Ctrl+V")
editmenu.add_separator()
editmenu.add_command(label="Select All", command=selAll, accelerator="Ctrl+A")
menubar.add_cascade(label="Edit", menu=editmenu)

papermenu = Menu(menubar, tearoff=0)
papermenu.add_command(label="Settings")
papermenu.add_separator()
papermenu.add_command(label="About Paper", command=aboutWindow)
menubar.add_cascade(label="Paper", menu=papermenu)

main_window.bind_all("<Control-o>", openfile_link)
main_window.bind_all("<Control-s>", save_link)
main_window.bind_all("<Control-q>", exitfunc)

###MAIN LOOP
main_window.mainloop()

