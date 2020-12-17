"""
use StringVar variables
lay out by columns: this might not align horizontally everywhere (see entry2)
"""

from tkinter import *
#from quitter import Quitter
#fields = 'Name', 'Job', 'Pay'
entryfont= ('Ariel', 13)

def fetch(variables):   #names, jobs, pay):    #variables,
    for variable in variables:
       print('Input => "%s"' % variable.get())     # get from var
       #print('Input => "%s"' % eval(variable))

    #for name in names:
    #    print('Input => "%s"' % name.get())     # get from var

def makeform(root):
    form = Frame(root)                              # make outer frame
    #left = Frame(form)                              # make two columns
    #rite = Frame(form)
    #form.pack(fill=X)
    ##left.grid(row=0, column=0)  #.pack(side=LEFT)
    #rite.grid(row=0, column=1)  #.pack(side=RIGHT, expand=YES, fill=X)       # grow horizontal

    variables = []
    #names = []
    #jobs = []
    #pay = []
    #for field in fields:
    labn = Label(root, width=5, text='name')      # add to columns
    entn = Entry(root)
    labn.grid(row=0, column=0)  #.pack(side=TOP)
    entn.grid(row=0, column=1)  #.pack(side=TOP, fill=X)                  # grow horizontal
    labn.config(font=entryfont)
    entn.config(font=entryfont)
    # lbl_Title.config(font=titlefont)
    var = StringVar()
    name = StringVar()
    #print(entn.get())  #DNW
    #eci_qty = DoubleVar()
    entn.config(textvariable=var)                # link field to var
    var.set('enter here')
    variables.append(var)                   #names.append(var)
    #variables.append('name')                   #names.append(var)
    labj = Label(root, width=5, text='job')      # add to columns
    entj = Entry(root)
    labj.grid(row=1, column=0)  #.pack(side=TOP)
    entj.grid(row=1, column=1)  #.pack(side=TOP, fill=X)                  # grow horizontal
    labj.config(font=entryfont)
    entj.config(font=entryfont)
    var = StringVar()
    entj.config(textvariable=var)                # link field to var
    var.set('enter here')
    variables.append(var)                   #jobs.append(var)
    lab_ElementQty1 = Label(root, width=5, text='quantity')
    lab_ElementQty1.grid(row=2, column=0)
    e_ElementQty1 = Entry(root, text=0, width=8)
    e_ElementQty1.grid(row=2, column=1, padx=4)
    lab_ElementQty1.config(font=entryfont)
    e_ElementQty1.config(font=entryfont)
    var = StringVar()
    e_ElementQty1.config(textvariable=var)
    variables.append(var)                   #pay.append(var)
    return variables

if __name__ == '__main__':
    root = Tk()
    vars = makeform(root)
    Button(root, text='Fetch', font=entryfont, command=(lambda: fetch(vars))).grid(row=3, column=0)  #.pack(side=LEFT)
    # Button.config(root, font=entryfont)
    #Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()
