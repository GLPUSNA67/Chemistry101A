"""
See peoplegui--old.py: the alternative here uses nedted row frames with fixed
widdth labels with pack() to acheive the same aligned layout as grid(), but it
takes two extra lines of code as is (though adding window resize support makes
the two techniques roughly the same--see later in the book).
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = 'class-element-shelve'
fieldnames = ('symbol', 'name', 'a_number', 'a_mass', 'group', 'period', 'column',
              'protons', 'neutrons', 'electrons', 'density', 'a_radius', 'affinity',  'electronegativity',
              'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit','char',
              '_1s', '_2s', '_2p', '_3s', '_3p', '_3d', '_4s', '_4p', '_4d', '_4f', '_5s', '_5p', '_5d', '_5f',
              '_6s', '_6p', '_6d', '_7s','reserved')
'''
symbol, name, a_number, a_mass, group, period, column,
                 protons, neutrons, electrons, density, a_radius, affinity,  electronegativity,
    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', '_1s', '_2s', '_2p', '_3s', '_3p', '_3d', '_4s', '_4p', '_4d', '_4f', 'reserved')
'''

def makeWidgets():
    global entries
    window = Tk()
    window.title('Element Shelve')
    form   = Frame(window)
    form.pack()
    entries = {}
    for label in ('key',) + fieldnames:
        row = Frame(form)
        lab = Label(row, text=label, width=6)
        ent = Entry(row)
        row.pack(side=TOP)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        entries[label] = ent
    Button(window, text="Fetch",  command=fetchRecord).pack(side=LEFT)
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit",   command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]                      # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]                      # update existing record
    else:
        from element import Element             # make/store new one for key
        record = Element(symbol='?', name='?')    # eval: strings must be quoted
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close() # back here after quit or window close
