
from tkinter import Y


def first():
    x  = "global variable"
    
    def name():
        nonlocal x
        x = "local variable"
        print (x) 

    name()
    print(x)


first()
