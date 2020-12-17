from tkinter import *
root = Tk()

variables = []
def radio1():
    #global eciRadio1
    eciRadio1 = IntVar()
    var = StringVar()
    #for i in range(10):
    radE = Radiobutton(root, text='Elements', variable=var, value='elements')
    radE.grid(row=0, column=0)
    radC = Radiobutton(root, text='Compounds', variable=var, value='compounds')
    radC.grid(row=0, column=1)
    radI = Radiobutton(root, text='Ions', variable=var, value='ions')
    radI.grid(row=0, column=2)
    eciRadio1.set(0) # deselect all initially
    variables.append(var)
    print("eciRadio1 is", eciRadio1)

def fetch(variables):   #names, jobs, pay):    #variables,
    for variable in variables:
       print('Input => "%s"' % variable.get())

radio1()
if __name__ == '__main__':
    #vars = makeform(root)
    Button(root, text='Fetch', command=(lambda: fetch(variables))).grid(row=3, column=0)  #.pack(side=LEFT)
    #Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(variables)))
root.mainloop()

