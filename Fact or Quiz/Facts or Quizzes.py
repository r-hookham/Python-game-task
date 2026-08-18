#Imports
import tkinter as tk
from tkinter import messagebox
import random
import subprocess

import Colour_palette
import Facts
import Quizzes

root = tk.Tk()
root.title("Facts or Quizzes Game")
root.geometry("400x500")
root.resizable(False, False)
fact_list = []

#Colour palette
foregroundcolour = Colour_palette.foregroundcolour
backgroundcolour = Colour_palette.backgroundcolour

#Fonts
headingfont = ("Arial", 12, "bold")
standardfont = ("Arial", 10)
paragraphfont = ("Arial", 8)
#Functions

def confirm():
    if game.get() == 0:
           tk.messagebox.showerror("Error", "Error 1: Please select a game before confirming.")
    elif topic.get() == "none":
        messagebox.showerror("Error", "Error 2: Please select a topic.")
    elif game.get() == 1:
        root.geometry("400x300")
        factgame()

    elif game.get() == 2:
        quizselection() 

def change_settings():
    global fact_list
    fact_list = []
    FactFrame.pack_forget()
    root.geometry("400x500")
    GameSelectFrame.pack(padx=5, pady=5)

def factgame():
    global fact_list

    if not fact_list:
        if topic.get() == "english":
            fact_list = Facts.english.copy()
        elif topic.get() == "maths":
            fact_list = Facts.maths.copy()
        elif topic.get() == "history":
            fact_list = Facts.history.copy()
        elif topic.get() == "science":
            fact_list = Facts.science.copy()
        elif topic.get() == "computer":
            fact_list = Facts.computer.copy()
    random.shuffle(fact_list)

    chosenfact.set(fact_list.pop())
    GameSelectFrame.pack_forget()
    FactFrame.pack(padx=5, pady=5)
    
def quizselection():
    if topic.get() == "english":
        chosenfact.set(random.choice(Quizzes.english))
    elif topic.get() == "maths":
        chosenfact.set(random.choice(Quizzes.maths))
    elif topic.get() == "history":
        chosenfact.set(random.choice(Quizzes.history))
    elif topic.get() == "science":
        chosenfact.set(random.choice(Quizzes.science))
    elif topic.get() == "computer":
        chosenfact.set(random.choice(Quizzes.computer))
        GameSelectFrame.pack_forget()
        QuizFrame.pack(padx=5, pady=5)

def colourpalette():
    subprocess.Popen(["notepad.exe", "Fact or Quiz/Colour_palette.py"])
    

#Tkinter GUI
root.config(
            bg = backgroundcolour
            )
game = tk.IntVar(value=0)
topic = tk.StringVar(value="none")
fact_list = []
chosenfact = tk.StringVar(value="")
GameSelectFrame = tk.Frame(root,
                            bg=backgroundcolour,                      
)
GameSelectFrame.pack(padx=2, pady=2)

tk.Label(GameSelectFrame, 
         text="Select a game mode:",
         font=headingfont,
         bg=backgroundcolour, 
         fg=foregroundcolour
         ).pack(padx=10, pady=10)

tk.Radiobutton(GameSelectFrame,
               text="Facts",
               font=standardfont,
               variable=game, 
               value=1,
               bg=backgroundcolour,
               fg=foregroundcolour,
               selectcolor=backgroundcolour,
               ).pack(padx=10, pady=2)
tk.Radiobutton(GameSelectFrame, 
               text="Quizzes",
               font=standardfont,
               variable=game, 
               value=2, 
               bg=backgroundcolour,
               fg=foregroundcolour,
               selectcolor=backgroundcolour,
               ).pack(padx=10, pady=2)

tk.Label(GameSelectFrame, 
         text="Select a topic:",
         font = headingfont,
         bg=backgroundcolour, 
         fg=foregroundcolour
         ).pack(padx=10, pady=10)

tk.Radiobutton(GameSelectFrame, 
               text="English",
               font=standardfont,
               variable=topic, 
               value="english", 
               bg=backgroundcolour, 
               fg=foregroundcolour,
               selectcolor=backgroundcolour,

).pack(padx=10, pady=2)

tk.Radiobutton(GameSelectFrame, 
               text="Maths",
               font=standardfont,
               variable=topic, 
               value="maths", 
               bg=backgroundcolour, 
               fg=foregroundcolour,
               selectcolor=backgroundcolour

).pack(padx=10, pady=2)

tk.Radiobutton(GameSelectFrame, 
               text="History",
               font=standardfont,
               variable=topic, 
               value="history", 
               bg=backgroundcolour, 
               fg=foregroundcolour,
               selectcolor=backgroundcolour,
).pack(padx=10, pady=2)
tk.Radiobutton(GameSelectFrame, text="Science", 
               variable=topic, 
               value="science",
               font=standardfont,
               bg=backgroundcolour, 
               fg=foregroundcolour,
               selectcolor=backgroundcolour,
               ).pack(padx=10, pady=2)
tk.Radiobutton(GameSelectFrame, text="Computer Tech", 
               variable=topic,
               value="computer",
               font=standardfont,
               bg=backgroundcolour,
               fg=foregroundcolour,
               selectcolor=backgroundcolour
               ).pack(padx=10, pady=2)


tk.Button(GameSelectFrame,
            text = "Confirm",
            fg = foregroundcolour,
            bg = backgroundcolour,
            
            command = confirm
            ).pack(padx=10, pady=5)

tk.Label(GameSelectFrame, 
         text="If you'd like to read multiple facts quickly, I'd recommend using tab and space to select next fact without having to mouse when the button moves.",
         font=paragraphfont,
         bg=backgroundcolour,
         fg=foregroundcolour,
         wraplength=360,

         ).pack(padx=10, pady=5)
tk.Label(GameSelectFrame, 
         text="If you'd like to use a different colour palette, change the colours in Colour_palette.py, or click the button below. (Only works on Windows)",
         font=paragraphfont,
         bg=backgroundcolour,
         fg=foregroundcolour,
         wraplength=360,
         ).pack(padx=10, pady=5)
tk.Button(GameSelectFrame,
          text="Click here to open the file.",
          font=paragraphfont,
          bg=backgroundcolour,
          fg=foregroundcolour,
          command = colourpalette
).pack(padx=10, pady=5)

FactFrame = tk.Frame(root,
                    bg=backgroundcolour,                      
)
tk.Label(FactFrame,
         text="Your fact is...",
         font = headingfont,
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()
tk.Label(FactFrame,
         textvariable=chosenfact,
         fg = foregroundcolour,
         bg = backgroundcolour,
         wraplength=360,
         justify="left",
         ).pack(padx=10, pady=10)

tk.Button(FactFrame,
            text = "Again",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = factgame,
            ).pack(padx = 10, pady = 5)

tk.Button(FactFrame,
            text = "Change settings",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = change_settings,
            justify="right",
            ).pack(padx = 10, pady = 5)

QuizFrame = tk.Frame(root,
                    bg=backgroundcolour,                      
)


tk.Label(QuizFrame,
         text="Your true/false question is...",
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()

tk.Label(QuizFrame,
         textvariable=chosenfact,
         fg = foregroundcolour,
         bg = backgroundcolour,
         wraplength=300,
         justify="left",
         ).pack(padx=10, pady=10)

tk.Button(QuizFrame,
            text = "True",
            fg = foregroundcolour,
            bg = backgroundcolour,
            #command = true,
            justify = "left"
            ).pack(padx = 10, pady = 5)

tk.Button(QuizFrame,
            text = "False",
            fg = foregroundcolour,
            bg = backgroundcolour,
            #command = false,
            justify="right",
            ).pack(padx = 10, pady = 5)


QuizFrameAnswer = tk.Frame(root,
                           bg=backgroundcolour
)

root.mainloop()