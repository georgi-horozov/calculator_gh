import re
from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("570x550")
root.configure(bg="#FFFFFF")

equation = ""


def show(num):
    global equation
    if num == "\u221A":
        equation += "math.sqrt("
    elif num == "%":
        # Handle percentage correctly
        parts = re.split(r'(\D)', equation)
        if len(parts) > 1 and parts[-2] in "+-*/":
            last_num = parts[-1]
            last_operator = parts[-2]
            percentage = str(float(last_num) * 0.01 * float(parts[-3])) if last_operator in "+-" else str(float(last_num) * 0.01)
            equation = "".join(parts[:-1]) + percentage
        else:
            equation += "*0.01"
    else:
        equation += num
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation

    result = ""

    if equation != "":
        try:
            equation_modified = equation + ")" * equation.count("math.sqrt(")
            result = eval(equation_modified)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

        except ZeroDivisionError:
            result = "Cannot divide by 0"
            equation = ""

        except SyntaxError:
            result = "Syntax Error"
            equation = ""
        else:
            equation = str(result)

    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text="", font=("arial", 30), bg="#F5F5DC")
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#000000", bg="#FFFF00", command=lambda: clear()).place(x=10, y=100)

Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("/")).place(x=150, y=100)

Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("%")).place(x=290, y=100)

Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("7")).place(x=10, y=190)

Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("8")).place(x=150, y=190)

Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("9")).place(x=290, y=190)

Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("-")).place(x=430, y=190)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("4")).place(x=10, y=280)

Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("5")).place(x=150, y=280)

Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("6")).place(x=290, y=280)

Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("+")).place(x=430, y=280)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("1")).place(x=10, y=370)

Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("2")).place(x=150, y=370)

Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("3")).place(x=290, y=370)

Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: calculate()).place(x=430, y=370)

Button(root, text="\u221A", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("\u221A")).place(x=10, y=460)

Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show("0")).place(x=150, y=460)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#FFFFFF", bg="#808080", command=lambda: show(".")).place(x=290, y=460)

root.mainloop()
