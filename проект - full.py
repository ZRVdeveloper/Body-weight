from tkinter import *
from customtkinter import *
import datetime

set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

mywin = CTk()
f = open("rez.txt","r")
F_exit = f.readlines()
l = F_exit[-3:]
#print (l)
a,b,kg  = map(float, l[2].split())
#a,b,kg  = 2, 3, 4
f.close()
name = StringVar(value = l[1])
vaga = IntVar(value = a)
zrist = IntVar(value = b)

mywin.geometry("450x350")
mywin.title("Маса тіла")
def button_function():
    h2 = (zrist.get()/100) * (zrist.get()/100)
    kg = round(vaga.get()/h2,2)
    if kg < 18 : label_3.config(text = f"Мала вага {kg}%", text_color = "yellow")
    elif kg > 18 and kg < 25: label_3.config(text = f"Достатня вага {kg}%", text_color = "green")   
    else: label_3.config(text = f"Зайва вага {kg}%", text_color = "red")
    print (kg)
    f = open("rez.txt","a")
    f.write(f"\n-------------------------\n{datetime.datetime.now()}\n{name.get()} \n{vaga.get()} {zrist.get()} {kg}")
    f.close()
    
    
frame_1 = CTkFrame(master=mywin, corner_radius=10)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

CTkLabel(master=frame_1, justify=LEFT, text = "Норма ваги",text_color = "#777", text_font = ("", 25)).pack()

label_0 = CTkLabel(master=frame_1, text = "Введіть ваше ім'я", text_font = ("", 14)).place(x=10, y=50)
label_1 = CTkLabel(master=frame_1, text = "Введіть свій зріст", text_font = ("", 14)).place(x=10, y=100)
label_2 = CTkLabel(master=frame_1, justify=LEFT, text = "Введіть масу тіла", text_font = ("", 14)).place(x=10, y=150)
label_3 = CTkLabel(master=frame_1, justify=LEFT, text = "",text_font = ("", 14))
label_3.place(x=0, y=200)

entry_1 = CTkEntry(master=frame_1, placeholder_text="Ім'я", textvariable = name)
entry_1.place(x=250, y=50)

entry_1 = CTkEntry(master=frame_1, placeholder_text="Зріст", textvariable = zrist)
entry_1.place(x=250, y=100)

entry_2 = CTkEntry(master=frame_1, placeholder_text="Вага", textvariable = vaga)
entry_2.place(x=250, y=150)

button_1 = CTkButton(master=frame_1, text="Порахувати", corner_radius=8, command=button_function)
button_1.place(x=250, y=200)

CTkLabel(master=frame_1, justify=LEFT, text = f"Остані заміри\n {l[0][:20]}",text_color = "#777", text_font = ("", 8)).place(x=250, y=250)

mywin.mainloop()