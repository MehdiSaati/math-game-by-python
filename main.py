from tkinter import *
import random
import time
import os
os.chdir("/Users/mahan/Desktop/day49")
THEME_COLOR = "#2192FF"
SCORE= 0
# ------------------------------- Get Next Number1 -----------------------------------#
def get_next_number():
    canvas.config(bg="gold") 
    score_label.config(text=f"امتیاز : {SCORE}", font=("Arial", 24, "bold")) 
    global NUM
    NUM = random.randint(0, 9)
    canvas.itemconfig(question_text, text=f"{NUM} ", font=("Arial", 46, "bold"))
# ------------------------------- Get Next Number2 -----------------------------------#
def get_next_number2():
    global NUM2
    NUM2 = random.randint(0, 9)
    canvas.itemconfig(question_text, text=f"{NUM2} ", font=("Arial", 46, "bold"))
    window.after(1000, answer)
# ------------------------------- Get Oprator -----------------------------------#
def get_oprator():
    global OP
    OP = random.choice(["+", "-", "*", "/"])
    canvas.itemconfig(question_text, text=f"{OP} ", font=("Arial", 46, "bold"))
    window.after(1000, get_next_number2)
# ------------------------------- Start -----------------------------------#
def start():
    get_next_number()
    window.after(1000, get_oprator)
# ------------------------------- Next -----------------------------------#
def next():
    USER_INPUT.destroy()
    start()
# ------------------------------- Answer -----------------------------------#
def answer():
    global RESULT, USER_INPUT
    canvas.config(bg="#FDFF00") 
    canvas.itemconfig(question_text, text=f"", font=("Arial", 46, "bold"))
    USER_INPUT =  Entry(width=10)
    USER_INPUT.focus_set()
    USER_INPUT.grid(column=0, row=1, columnspan=2)
    if OP == "*":
        RESULT = NUM * NUM2 
    elif OP =="+":
        RESULT = NUM + NUM2 
    elif OP =="-":
        RESULT = NUM - NUM2 
    elif OP =="/":
        RESULT = NUM / NUM2 

# ------------------------------- Check Answer -----------------------------------#
def check_answer():
    
    if int(RESULT) == int(USER_INPUT.get()):
        USER_INPUT.destroy()
        canvas.config(bg="#5cd552") 
        canvas.itemconfig(question_text, text=f"!آفرین درست گفتی\n{RESULT} ", font=("Arial", 24, "bold"))
        global SCORE
        SCORE += 1
        
        window.after(2000, start)
    else:
        USER_INPUT.destroy()
        canvas.config(bg="red") 
        canvas.itemconfig(question_text, text=f"!اشتباه\n{RESULT} ", font=("Arial", 24, "bold"))
        window.after(2000, start)

# ------------------------------- UI -----------------------------------#
window = Tk()
window.title("آموزش ریاضی")
window.config(padx=20, pady=20, bg=THEME_COLOR )

score_label = Label(text="امتیاز : 0", fg="white", bg=THEME_COLOR)
score_label.grid(row=0, column=0, pady=20, columnspan=2)

canvas = Canvas(width=300, height=250)

question_text = canvas.create_text(
    150,
    125,
    text="All program codes",
    fill=THEME_COLOR,
    font=("Ariel", 16, "italic"),
    width=280)  
canvas.grid(row=1, column=0 , columnspan=2, pady=50)

true_image = PhotoImage(file="images/true.png")
true_button = Button(image=true_image,command=check_answer, highlightthickness=0)
true_button.grid(row=2, column=0, pady=20)

false_image = PhotoImage(file="images/false.png")
false_button = Button(image=false_image,command=next, highlightthickness=0)
false_button.grid(row=2, column=1, pady=20)

start()

window.mainloop()
