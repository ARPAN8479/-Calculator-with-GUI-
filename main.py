import tkinter as tk

# -----------------------------
# Core Logic
# -----------------------------
expression = ""

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

input_text = tk.StringVar()

# Display
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=('Arial', 18),
    width=20,
    bd=5,
    relief=tk.RIDGE,
    justify='right'
)
input_field.grid(row=0, column=0)

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create Buttons
for i in range(4):
    for j in range(4):
        text = buttons[i][j]

        if text == "C":
            action = clear
        elif text == "=":
            action = equal
        else:
            action = lambda x=text: press(x)

        tk.Button(
            btn_frame,
            text=text,
            width=5,
            height=2,
            font=('Arial', 14),
            command=action
        ).grid(row=i, column=j, padx=5, pady=5)

# Run App
root.mainloop()
