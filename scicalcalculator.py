import tkinter as tk
import math
import ast
import operator


operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def safe_eval(expr):
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](eval_node(node.operand))
        else:
            raise ValueError("Invalid Expression")

    tree = ast.parse(expr, mode='eval')
    return eval_node(tree.body)

#Functions
def press(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = safe_eval(entry.get())
        clear()
        entry.insert(tk.END, result)
    except:
        clear()
        entry.insert(tk.END, "Error")

def sin():
    value = float(entry.get())
    clear()
    entry.insert(tk.END, round(math.sin(math.radians(value)), 6))

def cos():
    value = float(entry.get())
    clear()
    entry.insert(tk.END, round(math.cos(math.radians(value)), 6))

def tan():
    value = float(entry.get())
    clear()
    entry.insert(tk.END, round(math.tan(math.radians(value)), 6))

def log():
    value = float(entry.get())
    clear()
    entry.insert(tk.END, round(math.log10(value), 6))

def sqrt():
    value = float(entry.get())
    clear()
    entry.insert(tk.END, round(math.sqrt(value), 6))

#   Window
root = tk.Tk()
root.title("Safe Mobile Scientific Calculator")
root.geometry("360x600")
root.configure(bg="#1c1c1c")
root.resizable(False, False)

#Display
entry = tk.Entry(
    root,
    font=("Helvetica", 28),
    bg="#1c1c1c",
    fg="white",
    bd=0,
    justify="right"
)
entry.pack(fill=tk.BOTH, padx=20, pady=30, ipady=20)

#Button Frame
frame = tk.Frame(root, bg="#1c1c1c")
frame.pack()

btn = {
    "font": ("Helvetica", 16),
    "width": 5,
    "height": 2,
    "bd": 0
}

def make(text, r, c, cmd, bg="#333333"):
    tk.Button(frame, text=text, bg=bg, fg="white",
              command=cmd, **btn).grid(row=r, column=c, padx=8, pady=8)

# Scientific buttons
make("sin", 0, 0, sin, "#555555")
make("cos", 0, 1, cos, "#555555")
make("tan", 0, 2, tan, "#555555")
make("log", 0, 3, log, "#555555")

# Main buttons
layout = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

for t,r,c in layout:
    if t == "=":
        make(t, r, c, calculate, "#ff9500")
    else:
        make(t, r, c, lambda x=t: press(x))

make("√", 5, 0, sqrt, "#555555")
make("C", 5, 1, clear, "#ff3b30")

root.mainloop()
