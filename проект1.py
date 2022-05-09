from tkinter import *
from customtkinter import *

set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

mywin = CTk()
mywin.geometry("450x350")

vaga = IntVar(value = 70)
zrist = IntVar(value = 180)

def button_function():
    h2 = (zrist.get()/100) * (zrist.get()/100)
    kg = round(vaga.get()/h2,2)
    
    if kg < 18 : label_3.config(text = f"Мала вага {kg}%", text_color = "yellow")
    elif kg > 18 and kg < 25: label_3.config(text = f"Достатня вага {kg}%", text_color = "green")   
    else: label_3.config(text = f"Зайва вага {kg}%", text_color = "red")

frame_1 = CTkFrame(master=mywin, corner_radius=10)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

CTkLabel(master=frame_1, justify=LEFT, text = "Норма ваги",text_color = "#777", text_font = ("Arial", 25)).pack()

label_1 = CTkLabel(master=frame_1, text = "Введіть свій зріст", text_font = ("", 14)).place(x=10, y=100)
label_2 = CTkLabel(master=frame_1, justify=LEFT, text = "Введіть масу тіла", text_font = ("", 14)).place(x=10, y=150)
label_3 = CTkLabel(master=frame_1, justify=LEFT, text = "",text_font = ("", 14))
label_3.place(x=0, y=200)

entry_1 = CTkEntry(master=frame_1, placeholder_text="Зріст", textvariable = zrist)
entry_1.place(x=250, y=100)

entry_2 = CTkEntry(master=frame_1, placeholder_text="Вага", textvariable = vaga)
entry_2.place(x=250, y=150)

button_1 = CTkButton(master=frame_1, text="Порахувати", corner_radius=8, command=button_function)
button_1.place(x=250, y=200)

mywin.mainloop()