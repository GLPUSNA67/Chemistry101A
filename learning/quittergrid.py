"""
a Quit button that verifies exit requests;
to reuse, attach an instance to other GUIs, and re-pack as desired
"""

from tkinter import *                          # get widget classes
from tkinter.messagebox import askokcancel     # get canned std dialog

class Quitter(Frame):                          # subclass our GUI
    def __init__(self, parent=None):           # constructor method
        Frame.__init__(self, parent)
        self.grid(row=0, column=0)
        widget = Button(self, text='Quit', command=self.quit)
        widget.grid(row=2, column=0)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

if __name__ == '__main__':  Quitter().mainloop()
