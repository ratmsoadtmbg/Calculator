import tkinter as tk

current_input = ''
total = 0

def press_one():
    global current_input
    current_input += '1'
    update_display(current_input)

def press_two():
    global current_input
    current_input += '2'
    update_display(current_input)

def press_three():
    global current_input
    current_input += '3'
    update_display(current_input)

def press_four():
    global current_input
    current_input += '4'
    update_display(current_input)

def press_five():
    global current_input
    current_input += '5'
    update_display(current_input)

def press_six():
    global current_input
    current_input += '6'
    update_display(current_input)

def press_seven():
    global current_input
    current_input += '7'
    update_display(current_input)

def press_eight():
    global current_input
    current_input += '8'
    update_display(current_input)

def press_nine():
    global current_input
    current_input += '9'
    update_display(current_input)

def press_zero():
    global current_input
    current_input += '0'
    update_display(current_input)

def press_plus():
    global total, current_input
    if current_input:
        total += int(current_input)
        current_input = ''
        update_display(str(total))
    
def press_minus():
    global total, current_input
    if current_input:
        total -= int(current_input)
        current_input = ''
        update_display(str(total))

def press_times():
    global total, current_input
    if current_input:
        total *= int(current_input)
        current_input = ''
        update_display(str(total))

def press_divide():
    global total, current_input
    if current_input:
        total /= int(current_input)
        current_input = ''
        update_display(str(total))

def update_display(value):
    greeting_label.config(text=value)

window = tk.Tk()
window.geometry("400x500")
window.title("Calculator")

icon = tk.PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#C9FFFC")

greeting_label = tk.Label(window, text="", font=("Arial", 14), background="#6cbef9")
greeting_label.pack(pady=10)

button_one = tk.Button(window, text='1', command=press_one)
button_one.pack()
button_one = tk.Button(window, text='2', command=press_two)
button_one.pack()
button_one = tk.Button(window, text='3', command=press_three)
button_one.pack()
button_one = tk.Button(window, text='4', command=press_four)
button_one.pack()
button_one = tk.Button(window, text='5', command=press_five)
button_one.pack()
button_one = tk.Button(window, text='6', command=press_six)
button_one.pack()
button_one = tk.Button(window, text='7', command=press_seven)
button_one.pack()
button_one = tk.Button(window, text='8', command=press_eight)
button_one.pack()
button_one = tk.Button(window, text='9', command=press_nine)
button_one.pack()
button_one = tk.Button(window, text='0', command=press_zero)
button_one.pack()
button_plus = tk.Button(window, text='+', command=press_plus)
button_plus.pack()
button_plus = tk.Button(window, text='-', command=press_minus)
button_plus.pack()
button_plus = tk.Button(window, text='x', command=press_times)
button_plus.pack()
button_plus = tk.Button(window, text='/', command=press_divide)
button_plus.pack()

window.mainloop()