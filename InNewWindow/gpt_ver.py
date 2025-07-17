import tkinter as tk

current_input = ''
total = 0
last_operator = None
just_evaluated = False  # New flag

def update_display(value):
    greeting_label.config(text=value)

def add_to_input(digit):
    global current_input, just_evaluated
    if just_evaluated:
        current_input = ''
        just_evaluated = False
    current_input += digit
    update_display(current_input)

def operate(op):
    global total, current_input, last_operator, just_evaluated
    if current_input:
        if last_operator:
            perform_operation()
        else:
            total = int(current_input)
    last_operator = op
    current_input = ''
    just_evaluated = False

def perform_operation():
    global total, current_input, last_operator, just_evaluated
    if not current_input or not last_operator:
        return
    try:
        value = int(current_input)
        if last_operator == '+':
            total += value
        elif last_operator == '-':
            total -= value
        elif last_operator == '*':
            total *= value
        elif last_operator == '/':
            if value != 0:
                total /= value
            else:
                update_display("Error: Divide by 0")
                clear(keep_display=True)
                return
        update_display(str(int(total)))
        current_input = ''
        just_evaluated = True  # Flag that we just calculated
    except ValueError:
        pass

def equals():
    perform_operation()

def clear(keep_display=False):
    global current_input, total, last_operator, just_evaluated
    current_input = ''
    total = 0
    last_operator = None
    just_evaluated = False
    if not keep_display:
        update_display('0')

# --- Tkinter GUI setup ---
window = tk.Tk()
window.geometry("320x400")
window.title("Calculator")
window.config(background="#AD4444")

try:
    icon = tk.PhotoImage(file='logo.png')
    window.iconphoto(True, icon)
except:
    pass

greeting_label = tk.Label(window, text="", font=("Arial", 24), bg="#ffffff", anchor='e')
greeting_label.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky='we')

frame = tk.Frame(window,bg="#454545")
frame.grid(row=1, column=0, columnspan=4, pady=20, padx=10, sticky='we')

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('=', 4, 1), ('C', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit():
        action = lambda t=text: add_to_input(t)
    elif text == '=':
        action = equals
    elif text == 'C':
        action = clear
    else:
        action = lambda t=text: operate(t)

    tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14), command=action)\
        .grid(row=row, column=col, padx=5, pady=5)

update_display('0')

window.mainloop()
