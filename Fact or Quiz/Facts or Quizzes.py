#Imports
import tkinter as tk
from tkinter import messagebox #Allows for pop-up error boxes when program isn't used correctly, e.g. not selecting a game or topic
import random
import subprocess #Allows for the additional script that allows for changing the colour palette without 
import json #Allows for saving score and fact_count variables for future sessions
import os


import Colour_palette #Allows for easily customisable colours in a small, editable .py file
import Facts #Imports the fact list into the program so that all the fact lists can be saved as 'game_list'
import Quizzes 

root = tk.Tk()
root.title("Facts or Quizzes Game")
root.geometry("400x600") #Makes GUI larger to show all radiobutton options avaliable when on starting menu
root.resizable(False, False) #Keeps formatting the same regardless of whether user decides to use a tall, wide, small, large, or fullscreen window
game_list = [] #List of possible facts or quizzes at any one time

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "save.json")

#Colour palette
foregroundcolour = Colour_palette.foregroundcolour #Changes colours to align to the ones set in Colour_palette.py file
backgroundcolour = Colour_palette.backgroundcolour

#Fonts
headingfont = ("Arial", 12, "bold") #
standardfont = ("Arial", 10) #Font used for small titles
paragraphfont = ("Arial", 8) #Small font used for paragraphs

#Functions

def confirm():
    if game.get() == 0: 
           tk.messagebox.showerror("Error", "Error 1: Please select a game before confirming.")
    elif topic.get() == "none":
        messagebox.showerror("Error", "Error 2: Please select a topic.")
    elif game.get() == 1:
        root.geometry("400x300") #Makes GUI smaller to reduce empty space
        factgame() #Starts fact game

    elif game.get() == 2:
        root.geometry("400x300") #Makes GUI smaller to reduce empty space
        quizgame() #Starts quiz game

def change_settings():
    global game_list #imports the global list game_list to continue being used inside and outside of this function
    game_list = []
    root.geometry("400x600") #Makes GUI larger to show all radiobutton options avaliable
    FactFrame.pack_forget() #Hides previous frames
    QuizFrame.pack_forget()
    QuizFrameAnswer.pack_forget()
    GameSelectFrame.pack() #Displays selection frame to allow user to adjust settings

def factgame():
    global game_list

    if not game_list:
        if topic.get() == "english":
            game_list = Facts.english
        elif topic.get() == "maths":
            game_list = Facts.maths
        elif topic.get() == "history":
            game_list = Facts.history
        elif topic.get() == "science":
            game_list = Facts.science
        elif topic.get() == "computer":
            game_list = Facts.computer
    random.shuffle(game_list) #Shuffles the list of facts or quizzes into a random order

    chosen_item.set(game_list.pop()) #Selects an item from the fact list and sets variable 'chosen_item' so it can be shown in the label on the gameframe
    GameSelectFrame.pack_forget() #Hides previous frame
    FactFrame.pack() #Shows fact frame

    fact_count.set(fact_count.get() + 1)
    save_data()

def quizgame():
    QuizFrameAnswer.pack_forget()
    QuizFrame.pack()
    if topic.get() == "english":
        if random.getrandbits(1) == 1: #Selects random integer between the amount of bits specified (in this case, 1 bit or 2 values)
            quiz_answer.set(1)
            chosen_item.set(random.choice(Quizzes.true_english)) #Uses a true English question
        else: #Effectively 'if random.getrandbits(1) == 0:'
            quiz_answer.set(2)
            chosen_item.set(random.choice(Quizzes.false_english)) #Uses a false English question
    elif topic.get() == "maths":
        if random.getrandbits(1) == 1:
            quiz_answer.set(1)
            chosen_item.set(random.choice(Quizzes.true_maths))
        else:
            quiz_answer.set(2)
            chosen_item.set(random.choice(Quizzes.false_maths))
    elif topic.get() == "history":
        if random.getrandbits(1) == 1:
            quiz_answer.set(1)
            chosen_item.set(random.choice(Quizzes.true_history))
        else:
            quiz_answer.set(2)
            chosen_item.set(random.choice(Quizzes.false_history))

    elif topic.get() == "science":
        if random.getrandbits(1) == 1:
            quiz_answer.set(1)
            chosen_item.set(random.choice(Quizzes.true_science))
        else:
            quiz_answer.set(2)
            chosen_item.set(random.choice(Quizzes.false_science))
    elif topic.get() == "computer":
        if random.getrandbits(1) == 1:
            quiz_answer.set(1)
            chosen_item.set(random.choice(Quizzes.true_maths))
        else:
            quiz_answer.set(2)
            chosen_item.set(random.choice(Quizzes.false_maths))
    GameSelectFrame.pack_forget() #Hides main menu frame
    QuizFrame.pack() #Shows game frame

def true_answer():
    QuizFrame.pack_forget()
    player_answer.set(1)
    answer()

def false_answer():
    QuizFrame.pack_forget()
    player_answer.set(2)
    answer()

def answer():    
    if quiz_answer.get() == player_answer.get():
        printed_answer.set("Correct!")
        score.set(score.get() + 1)
    else:
        printed_answer.set("Incorrect...")
        score.set(score.get() - 1)
    save_data()
    QuizFrameAnswer.pack()

def save_data(): 
    data_to_save = {
        "score": score.get(),
        "fact_count": fact_count.get()
    }

    with open(FILE_PATH, "w") as json_file:
        json.dump(data_to_save, json_file, indent=4)

    print("Data saved successfully.")


def load_data():
    # Only try to load if the file actually exists
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as json_file:
            loaded_data = json.load(json_file)
    else:
        data_to_save = {
            "score": 0,
            "fact_count": 0
        }

        with open(FILE_PATH, "w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

        print("No save file found. Created a new save file.")
        # Inject the values back into Tkinter fields using .set()
        score.set(loaded_data.get("score", 0))
        fact_count.set(loaded_data.get("fact_count", 0))

        print("Data loaded successfully.")
    else:
        print("No saved data found.")


def colourpalette():
    subprocess.Popen(["notepad.exe", "Fact or Quiz/Colour_palette.py"]) #Opens notepad to the colour_palette.py file, allowing them to change the colours used in the program.
    

#Tkinter GUI
root.config(
            bg = backgroundcolour
            )
game = tk.IntVar(value=0)
topic = tk.StringVar(value="none")
quiz_answer = tk.IntVar(value=0)
player_answer = tk.IntVar(value=0)
printed_answer = tk.StringVar(value="none")
game_list = []
chosen_item = tk.StringVar(value="")
score = tk.IntVar(value=0)
fact_count = tk.IntVar(value=0)

load_data()

GameSelectFrame = tk.Frame(root,
                            bg=backgroundcolour,                      
)
GameSelectFrame.pack() #Displays selection frame to allow user to adjust settings

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
#Radiobuttons to select one game
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
#Radiobuttons to select one topic

tk.Button(GameSelectFrame,
            text = "Confirm",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = confirm
            ).pack(padx=10, pady=10)
tk.Label(GameSelectFrame,
         text=f"You've seen this many facts:",
         font = headingfont,
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()
tk.Label(GameSelectFrame,
         textvariable=fact_count,
         fg = foregroundcolour,
         bg = backgroundcolour,
         font = standardfont,
         ).pack()
tk.Label(GameSelectFrame,
         text="Your quiz score is:",
         font = headingfont,
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()
tk.Label(GameSelectFrame,
         textvariable=score,
         fg = foregroundcolour,
         bg = backgroundcolour,
         font = standardfont,
         ).pack()


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
         text="Your fact is:",
         font = headingfont,
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()
tk.Label(FactFrame,
         textvariable=chosen_item,
         fg = foregroundcolour,
         bg = backgroundcolour,
         wraplength = 360,
         ).pack()
tk.Label(FactFrame,
         text=f"You've seen this many facts:",
         font = headingfont,
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()
tk.Label(FactFrame,
         textvariable=fact_count,
         fg = foregroundcolour,
         bg = backgroundcolour,
         font = standardfont,
         ).pack()
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
         text="Your true/false question is:",
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()

tk.Label(QuizFrame,
         textvariable=chosen_item,
         fg = foregroundcolour,
         bg = backgroundcolour,
         wraplength=300,
         justify="left",
         ).pack(padx=10, pady=10)

tk.Button(QuizFrame,
            text = "True",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = true_answer,
            justify = "left"
            ).pack(padx = 10, pady = 5)

tk.Button(QuizFrame,
            text = "False",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = false_answer,
            justify="right",
            ).pack(padx = 10, pady = 5)


QuizFrameAnswer = tk.Frame(root,
                           bg=backgroundcolour
)
tk.Label(QuizFrameAnswer,
         text="You got that question:",
         fg = foregroundcolour,
         bg = backgroundcolour,
         font = headingfont,
         ).pack()
tk.Label(QuizFrameAnswer,
         textvariable=printed_answer,
         fg = foregroundcolour,
         bg = backgroundcolour,
         font = standardfont,
         ).pack(padx=10, pady=10)
tk.Label(QuizFrameAnswer,
         text="Your quiz score is:",
         font = headingfont,
         fg = foregroundcolour,
         bg = backgroundcolour,
         ).pack()
tk.Label(QuizFrameAnswer,
         textvariable=score,
         fg = foregroundcolour,
         bg = backgroundcolour,
         font = standardfont,
         ).pack()
tk.Button(QuizFrameAnswer,
            text = "Again",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = quizgame,
            ).pack(padx = 10, pady = 5)

tk.Button(QuizFrameAnswer,
            text = "Change settings",
            fg = foregroundcolour,
            bg = backgroundcolour,
            command = change_settings,
            justify="right",
            ).pack(padx = 10, pady = 5)
root.mainloop()