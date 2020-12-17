from tkinter import *
from quittergrid import Quitter

def fetch():
    print('Input => "%s"' % ent.get())             # get text

root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')                   # set text
ent.grid(row=1, column=0)

ent.focus()                                        # save a click
ent.bind('<Return>', (lambda event: fetch()))      # on enter key
btn = Button(root, text='Fetch', command=fetch)    # and on button
btn.grid(row=2, column=0)
Quitter(root).grid(row=3, column=0)
root.mainloop()
