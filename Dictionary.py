
from tkinter import *

# import json

import json
root=Tk()
root.title('Dictionary')
root.config(bg='gray15')
root.geometry('1500x650+0+0')


###################################

data= json.load(open("data.json"))

###################################

def click():

    display.config(state=NORMAL)

    text = entry.get()
    entry.delete(0,END)

    display.delete(0.0,END)
    
    try:

# exception handling

        definition = data[text]
        display.insert(END,definition)
        display.config(state=DISABLED)

    except:
        definition = 'Information regrading the text entered is not available!!!'
        display.insert(END,definition)


####################################

# create a grid 50 x 50 in the main window

c = 0

while c < 50:
    root.columnconfigure(c,weight=1)
    root.rowconfigure(c,weight=1)

    c += 1

    Label(root,text='DICTIONARY',font=('arial',40,'bold'),fg='black',relief=GROOVE).grid(row=11,column=18)

    Label(root,text='ENTER ANY WORD',font=('arial'),fg='black',relief=GROOVE).grid(row=16,column=17)

    entry=Entry(root,width=45,relief=GROOVE)

    entry.grid(row=16, column=18)

    entry.focus()

# create a button

    button=Button(root,text='SEARCH',font=('arial',15),fg='blue',relief=RIDGE,command=lambda:click()).grid(column=29, row=16)

c = 0

while c < 50:
    root.columnconfigure(c,weight=1)
    root.rowconfigure(c,weight=1)

    c += 1

    Label(root,text='DEFINITION',font=('arial',40,'bold'),fg='black',relief=GROOVE).grid(row=23,column=18)
    display=Text(root,height=15,width=90,relief=GROOVE)
    display.grid(row=30,column=18)

root.mainloop()




























