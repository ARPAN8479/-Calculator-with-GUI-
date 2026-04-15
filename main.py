import tkinter as tk

# -----------------------------
# Core Logic
# -----------------------------
expression = ""

def press(key):
    global expression
    expression += str(key)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        history_list.insert(0, expression + " = " + result)
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# -----------------------------
# UI Setup
# -----------------------------
root = tk.Tk()
root.title("Pro Calculator")
root.geometry("420x500")
root.config(bg="#121212")
root.resizable(False, False)

display_var = tk.StringVar()

# Display
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 24),
    bg="#1e1e1e",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Main Frame
main_frame = tk.Frame(root, bg="#121212")
main_frame.pack()

# Button Frame
btn_frame = tk.Frame(main_frame, bg="#121212")
btn_frame.grid(row=0, column=0)

# History Frame
history_frame = tk.Frame(main_frame, bg="#121212")
history_frame.grid(row=0, column=1, padx=10)

history_label = tk.Label(
    history_frame,
    text="History",
    fg="white",
    bg="#121212",
    font=("Segoe UI", 12)
)
history_label.pack()

history_list = tk.Listbox(
    history_frame,
    height=15,
    width=18,
    bg="#1e1e1e",
    fg="white",
    bd=0
)
history_list.pack()

# -----------------------------
# Button Style
# -----------------------------
def create_btn(text, row, col, cmd, color="#2d2d2d"):
    btn = tk.Button(
        btn_frame,
        text=text,
        width=5,
        height=2,
        font=("Segoe UI", 14),
        bg=color,
        fg="white",
        bd=0,
        command=cmd
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

    # Hover effect
    def on_enter(e):
        btn.config(bg="#444")

    def on_leave(e):
        btn.config(bg=color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# -----------------------------
# Buttons Layout
# -----------------------------
buttons = [
    ('7', lambda: press('7')), ('8', lambda: press('8')), ('9', lambda: press('9')), ('/', lambda: press('/')),
    ('4', lambda: press('4')), ('5', lambda: press('5')), ('6', lambda: press('6')), ('*', lambda: press('*')),
    ('1', lambda: press('1')), ('2', lambda: press('2')), ('3', lambda: press('3')), ('-', lambda: press('-')),
    ('0', lambda: press('0')), ('.', lambda: press('.')), ('=', equal), ('+', lambda: press('+'))
]

row = 0
col = 0
for text, cmd in buttons:
    create_btn(text, row, col, cmd)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Extra buttons
create_btn("C", 4, 0, clear, "#d9534f")
create_btn("⌫", 4, 1, backspace, "#f0ad4e")

# -----------------------------
# Keyboard Support
# -----------------------------
def key_event(event):
    key = event.char
    if key in "0123456789+-*/.":
        press(key)
    elif key == "\r":
        equal()
    elif key == "\x08":
        backspace()

root.bind("<Key>", key_event)

# Run App
root.mainloop()