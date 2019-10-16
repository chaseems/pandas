#!/usr/bin/env python
"""
This Python code for parse the address strings.
Version: 0.1
Last Edit: 2019-Oct-16
Author: Chase
Email: 
Notice: Before running this script, be sure the Libpostal libarry installed.
"""

import tkinter as tk
from tkinter import *
from postal.parser import parse_address
from postal.expand import *

window = tk.Tk()
window.title('Libpostal Address Parse')
window.geometry('800x600')

def expand_addr(self):
    """Method for expand the address, and insert the results to listbox"""
    
    # clear the listbox
    list_box_spend.delete(0,'end')
    # expand the address string
    list_addr = expand_address(var_addr.get())
    
    # insert the results list to the listbox
    for item in list_addr:
        list_box_spend.insert('end',item)

def parse_addr(addr):
    """Method for parse the address string"""

    # clear the listbox
    list_box_parse.delete(0,'end')
    # parse the address string
    addr = parse_address(addr)
    # conversion the results to dict, and reverse the value-key order
    dict_addr = dict((x[1], x[0]) for x in addr[0:])
    
    # insert the results dict to the listbox
    for key in dict_addr:
        list_box_parse.insert('end','{}: {}'.format(key,dict_addr[key]))

def cur_select(self):
    """Method for get the item of listbox which selected"""
    
    # get the item's value which selected
    addr = list_box_spend.get(list_box_spend.curselection())
    # parse the address and fill to listbox
    parse_addr(addr)

var_addr = tk.StringVar()
var02 = tk.StringVar()

"""GUI"""
lab01 = tk.Label(window,text='Address:')

entry = tk.Entry(window,textvariable=var_addr,show=None,font=('Arilal',14))
entry.bind("<Return>",expand_addr)


lab_parse = tk.Label(window,text='Parsed: ')
lab_spend = tk.Label(window,text='Normalization: ')

list_box_spend = tk.Listbox(window)
list_box_parse = tk.Listbox(window,listvariable=var02)
list_box_spend.bind('<<ListboxSelect>>',cur_select)

lab01.grid(row=0,column=0,sticky=E)
entry.grid(row=0,column=1,columnspan=4,sticky=E+W)

lab_spend.grid(row=1,column=0,columnspan=3,sticky=E+W,padx=100,ipadx=200)
lab_parse.grid(row=1,column=3,columnspan=2,sticky=E+W,padx=100,ipadx=200)

list_box_spend.grid(row=2,column=0,columnspan=3,sticky=N+S+E+W)
list_box_parse.grid(row=2,column=3,columnspan=2,sticky=N+S+E+W)

window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)
window.grid_columnconfigure(4,weight=1)
window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=1)
window.grid_rowconfigure(2,weight=30)
"""GUI"""

window.mainloop()
