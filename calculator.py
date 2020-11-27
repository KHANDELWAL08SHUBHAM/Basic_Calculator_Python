from tkinter import *
import tkinter.font as font

root = Tk()


root.title("Simple Calculator")

e = Entry(root, width = 45 , borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3 ,padx=10,pady=10)

font.Font(size=30)
myFont = font.Font(size=15)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)



def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)




def button_equal():
    second_num = e.get()
    global s_num
    s_num = int(second_num)
    e.delete(0,END)
    if math == "addition":
         e.insert(0, f_num + s_num)
    elif math == "subtraction":
         e.insert(0, f_num - s_num)
    elif math == "multiplication":
         e.insert(0, f_num * s_num)
    elif math == "division":
         e.insert(0, int(f_num / s_num))


but1= Button(root, text = "1" , padx = 40, pady = 20 , command = lambda: button_click(1))
but2 = Button(root, text = "2" , padx = 40, pady = 20 , command = lambda: button_click(2))
but3 = Button(root, text = "3" , padx = 40, pady = 20 , command = lambda: button_click(3))
but4 = Button(root, text = "4" , padx = 40, pady = 20 , command = lambda: button_click(4))
but5 = Button(root, text = "5" , padx = 40, pady = 20 , command = lambda: button_click(5))
but6 = Button(root, text = "6" , padx = 40, pady = 20 , command = lambda: button_click(6))
but7 = Button(root, text = "7" , padx = 40, pady = 20 , command = lambda: button_click(7))
but8 = Button(root, text = "8" , padx = 40, pady = 20 , command = lambda: button_click(8))
but9 = Button(root, text = "9" , padx = 40, pady = 20 , command = lambda: button_click(9))
but0 = Button(root, text = "0" , padx = 40, pady = 20 , command = lambda: button_click(0))
but_add = Button(root, text = "+" , padx = 40, pady = 20 , command = button_add)
but_sub = Button(root, text = "-" , padx = 40, pady = 20 , command = button_sub)
but_mul = Button(root, text = "*" , padx = 40, pady = 20 , command = button_mul)
but_div = Button(root, text = "/" , padx = 40, pady = 20 , command = button_div)
but_equal = Button(root, text = "=" , padx = 130, pady = 20 , command = button_equal)
but_clear = Button(root, text = "clear" , padx = 30, pady = 20 , command = button_clear)

but1['font'] = myFont
but2['font'] = myFont
but3['font'] = myFont
but4['font'] = myFont
but5['font'] = myFont
but6['font'] = myFont
but7['font'] = myFont
but8['font'] = myFont
but9['font'] = myFont
but0['font'] = myFont
but_add['font'] = myFont
but_sub['font'] = myFont
but_mul['font'] = myFont
but_div['font'] = myFont
but_equal['font'] = myFont
but_clear['font'] = myFont



but1.grid(row=3 ,column=0 )
but2.grid(row=3 ,column=1 )
but3.grid(row=3 ,column=2 )
but4.grid(row=2 ,column=0 )
but5.grid(row=2 ,column=1 )
but6.grid(row=2 ,column=2 )
but7.grid(row=1,column=0 )
but8.grid(row=1,column=1 )
but9.grid(row=1 ,column=2 )
but0.grid(row=4 ,column= 0)

but_add.grid(row=4 ,column= 1)
but_sub.grid(row=4 ,column= 2)
but_mul.grid(row=5 ,column= 0)
but_div.grid(row=5 ,column= 1)
but_clear.grid(row=5 ,column= 2)
but_equal.grid(row=6 ,column= 0, columnspan = 3)




root.mainloop()

