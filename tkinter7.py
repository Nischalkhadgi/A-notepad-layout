from tkinter import *


def doNothing():
    print("Sure")

root = Tk()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label = "New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_cascade(label="Redo", command=doNothing)

viewMenu = Menu(menu)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_cascade(label="Zoom In", command=doNothing)
viewMenu.add_cascade(label="Zoom Out", command=doNothing)

searchMenu = Menu(menu)
menu.add_cascade(label="Search", menu=searchMenu)
searchMenu.add_cascade(label="Find", command=doNothing)

terminalMenu = Menu(menu)
menu.add_cascade(label="Terminal", menu=terminalMenu)
terminalMenu.add_command(label="Reset", command=doNothing)

helpMenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_cascade(label="Contents", command=doNothing)
helpMenu.add_cascade(label="About", command=doNothing)

# toolbar
toolbar = Frame(root, bg="purple")
insertButton = Button(toolbar, text="Insert Image", command = doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2 )
printButton = Button(toolbar, text="Print", command = doNothing)
printButton.pack(side=LEFT, padx=2, pady=2 )
settingsButton = Button(toolbar, text="Settings", command = doNothing)
settingsButton.pack(side=LEFT, padx=2,pady=2)
designButton = Button(toolbar, text="Design", command = doNothing)
designButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#text
S = Scrollbar(root)
T = Text(root, height=10, width=45)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote="This is a demo of Notepad++ and as well as \n of terminal. Here you can just see the text \n and some button which have sub button. Which is working but not giving \n the exact output."
T.insert(END, quote)

#status bar

#Status = Label(root, text="Pending...", bd=1, relief=SUNKEN, anchor=W)
#Status.pack(side=BOTTOM, fill=X)

root.mainloop()

