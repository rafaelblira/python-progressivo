import sys
from tkinter import *
#from PIL import Image, ImageTk

def clear():
    txtDisplay.delete(0,END);
    return;

#Parent Window.
root = Tk();
root.title('Calculator - Rafael');
root.geometry('370x500');

#Main entry.
num1 = StringVar();
txtDisplay = Entry(root, textvariable = num1, relief=RIDGE, bd = 10, width=33,    insertwidth = 1, font = 40);
txtDisplay.place(x=15, y=10);
txtDisplay.focus();


def update_entry(v):
    current_value = num1.get()
    num1.set(current_value + v)

#Buttons:
zeroButton = Button(root, text='0', width=20, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('0')).place(x=17,y=382);
oneButton = Button(root, text='1', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('1')).place(x=17, y=302);
twoButton = Button(root, text='2', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('2')).place(x=100, y=302);
threeButton = Button(root, text='3', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('3')).place(x=182, y=302);
fourButton = Button(root, text='4', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('4')).place(x=17, y=222);
fiveButton = Button(root, text='5', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('5')).place(x=100, y=222);
sixButton = Button(root, text='6', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('6')).place(x=182, y=222);
sevenButton = Button(root, text='7', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('7')).place(x=17, y=142);
eightButton = Button(root, text='8', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('8')).place(x=100, y=142);
ninthButton = Button(root, text='9', width=8, height=3, bg='LightBlue', fg='red', command = lambda: update_entry('9')).place(x=182, y=142);

decimalButton = Button(root, text='.', width=8, height=3, bg='powder blue', command = lambda: update_entry('.')).place(x=182, y=382);
equalButton = Button(root, text='=', width=6, height=9, bg='Lightgreen', command = lambda: update_entry('=')).place(x=280, y=300);
plusButton = Button(root, text='+', width=8, height=3, bg='gray', command = lambda: update_entry('+')).place(x=264, y=222);
minusButton = Button(root, text='-', width=8, height=3, bg='gray', command = lambda: update_entry('-')).place(x=264, y=142);
multiplyButton = Button(root, text='x', width=8, height=3, bg='gray', command = lambda: update_entry('*')).place(x=264, y=66);
divideButton = Button(root, text='÷', width=8, height=3, bg='gray', command = lambda: update_entry('/')).place(x=182, y=66);
clearButton = Button(root, text='Clear (CE)', width=20, height=3, command =      clear, bg='Orange').place(x=17, y=66);

#Locks the parent windows size.
root.maxsize(370,500);
root.minsize(370,500);

#Parent window's background color:
root.configure(background = 'black');
root.mainloop();