import tkinter as tk

current_input = ''
total = 0

def add_to_input(digit):
    global current_input
    current_input += digit
    update_display(current_input)

def operate(op):
    global total, current_input
    if current_input:
        match op:
            case '+':
                total += int(current_input)
            case '-':
                total -= int(current_input)
            case '*':
                total *= int(current_input)
            case '/':
                total /= int(current_input)
        current_input = ''
        update_display(str(total))

def update_display(value):
    greeting_label.config(text=value)

def clear():
    global total
    total = 0
    update_display('0')

window = tk.Tk()
window.geometry("320x500")
window.title("Calculator")
window.config(background="#BFFF9A")

try:
    icon = tk.PhotoImage(file='logo.png')
    window.iconphoto(True, icon)
except:
    pass

greeting_label = tk.Label(window, text="", font=("Arial", 14), bg="#ffffff", anchor='e')
greeting_label.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky='we')

frame = tk.Frame(window, background="#999999")
frame.grid(row=1, column=0, columnspan=4, pady=20, padx=10,)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('0',4,0),('C',4,1),('=',4,2),('/',4,3)
]

for text,row,column in buttons:
    if text.isdigit():
        action = lambda t=text: add_to_input(t)
    elif text == '=':
        action = lambda: update_display(str(total))
    elif text == 'C':
        action = clear
    else:
        action = lambda t=text: operate(t)

    tk.Button(frame, text=text, width=5, height=3, font=('Arial', 14), command=action)\
        .grid(row=row, column=column, padx=5, pady=5)

update_display('0')

window.mainloop()