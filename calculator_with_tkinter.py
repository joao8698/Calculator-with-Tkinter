''' Calculadora com Interface Grafica Tkinter '''
from tkinter import *

#########################################
equation_text = ''

def button_press(num):
    global equation_text
    equation_text += str(num)
    calculeLabel.config(text=equation_text, padx=0, pady=0)

def equals_press():
    global equation_text
    try:
        result = str(eval(equation_text))
        calculeLabel.config(text=result)
        equation_text = result
    except Exception:
        calculeLabel.config(text="Erro")
        equation_text = ''

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    calculeLabel.config(text=equation_text)

################ JANELA ###################

window = Tk()
window.title('CALCULADORA')

#########################################

display_frame = Frame(window)
display_frame.grid(row=0, column=0)

calculeLabel = Label(display_frame,
                     bd=5,
                     relief=SUNKEN,
                     width=35,
                     height=3,
                     font=('Arial', 25, 'bold'))
calculeLabel.grid(row=0, column=0)

backspacebutton = Button(display_frame, text='<', command=backspace, height=8)
backspacebutton.grid(row=0, column=1)

#########################################

frame1 = Frame(window)
frame1.config(bd=5,
              relief=SUNKEN)
frame1.grid(row=1, column=0)

add1 = Button(frame1, text='1', width=9, height=3, command=lambda: button_press(1), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add1.grid(row=0, column=0)
add2 = Button(frame1, text='2', width=9, height=3, command=lambda: button_press(2), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add2.grid(row=0, column=1)
add3 = Button(frame1, text='3', width=9, height=3, command=lambda: button_press(3), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add3.grid(row=0, column=2)
add4 = Button(frame1, text='4', width=9, height=3, command=lambda: button_press(4), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add4.grid(row=1, column=0)
add5 = Button(frame1, text='5', width=9, height=3, command=lambda: button_press(5), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add5.grid(row=1, column=1)
add6 = Button(frame1, text='6', width=9, height=3, command=lambda: button_press(6), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add6.grid(row=1, column=2)
add7 = Button(frame1, text='7', width=9, height=3, command=lambda: button_press(7), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add7.grid(row=2, column=0)
add8 = Button(frame1, text='8', width=9, height=3, command=lambda: button_press(8), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add8.grid(row=2, column=1)
add9 = Button(frame1, text='9', width=9, height=3, command=lambda: button_press(9), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add9.grid(row=2, column=2)
add0 = Button(frame1, text='0', width=9, height=3, command=lambda: button_press(0), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
add0.grid(row=3, column=1)

equals_button = Button(frame1, text='=', width=9, height=3, command=equals_press, bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
equals_button.grid(row=3, column=2)

plus_button = Button(frame1, text='+', width=9, height=3, command=lambda: button_press('+'), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
plus_button.grid(row=0, column=4)

mines_button = Button(frame1, text='-', width=9, height=3, command=lambda: button_press('-'), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
mines_button.grid(row=1, column=4)

divide_button = Button(frame1, text='/', width=9, height=3, command=lambda: button_press('/'), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
divide_button.grid(row=2, column=4)

multiplies_button = Button(frame1, text='x', width=9, height=3, command=lambda: button_press('*'), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
multiplies_button.grid(row=3, column=4)

dot_button = Button(frame1, text='.', width=9, height=3, command=lambda: button_press('.'), bd=3, relief=RAISED, font=('Arial', 25, 'bold'))
dot_button.grid(row=3, column=0)

#########################################

window.mainloop()
