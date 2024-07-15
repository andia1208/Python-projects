from tkinter import *

#let's define 3 functions
def button_press(num):

    global equation_text
#combine all the numbers and symbols together to press
    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total  #to reuse the total and do other operations

    except SyntaxError:    #if you press only arithemitc symbols, and equal, them displays an error

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:   #not allow the division 0

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

#let's create a window
window = Tk()
window.title("My Calculator program")
window.geometry("800x800")

#let's create a string
equation_text = ""

#let's create a yellow label in the window of the calculator that will display the numbers we are entering in
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="yellow", width=43, height=2)
label.pack()

#Now we will create the buttons but we need to create a frame where to put the buttons
frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=10, font=40, bg="green", command=lambda: button_press(1))
button1.grid(row=0, column=0)     #we put the button in the frame


button2 = Button(frame, text=2, height=4, width=10, font=40, bg="green", command=lambda: button_press(2))  #command related to the function
button2.grid(row=0, column=1)


button3 = Button(frame, text=3, height=4, width=10, font=40, bg="green", command=lambda: button_press(3))
button3.grid(row=0, column=2)


button4 = Button(frame, text=4, height=4, width=10, font=40, bg="green", command=lambda: button_press(4))
button4.grid(row=1, column=0)


button5 = Button(frame, text=5, height=4, width=10, font=40, bg="green", command=lambda: button_press(5))
button5.grid(row=1, column=1)


button6 = Button(frame, text=6, height=4, width=10, font=40, bg="green", command=lambda: button_press(6))
button6.grid(row=1, column=2)


button7 = Button(frame, text=7, height=4, width=10, font=40,bg="green", command=lambda: button_press(7))
button7.grid(row=2, column=0)


button8 = Button(frame, text=8, height=4, width=10, font=40, bg="green", command=lambda: button_press(8))
button8.grid(row=2, column=1)


button9 = Button(frame, text=9, height=4, width=10, font=40, bg="green", command=lambda: button_press(9))
button9.grid(row=2, column=2)


button0 = Button(frame, text=0, height=4, width=10, font=40, bg="green", command=lambda: button_press(0))
button0.grid(row=3, column=1)


plus = Button(frame, text='+', height=4, width=10, font=35, bg="orange", command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=10, font=35,bg="orange", command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=10, font=35,bg="orange", command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=10, font=35, bg="orange", command=lambda: button_press('/'))
divide.grid(row=3, column=3)

decimal = Button(frame, text='.', height=4, width=10, font=35, bg="orange", command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

equal = Button(frame, text='=', height=4, width=10, font=35, bg="orange", command=equals)
equal.grid(row=3, column=2)

clear = Button(window, text='clear', height=4, width=43, font=35,bg="blue", command=clear)
clear.pack()


window.mainloop()
