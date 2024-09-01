from tkinter import *
from deep_translator import GoogleTranslator
from gtts import gTTS

def translate_lang():
    n1 = entry_window.get()
    n3 = drop_down.get()

    if n3 == "Hindi":
        change = "hi"
    elif n3 == "English":
        change = "en"
    elif n3 == "Japanese":
        change = "ja"
    elif n3 == "Malayalam":
        change = "ml"
    

    text_translate = GoogleTranslator(source='auto', target=change).translate(n1)


    two_label.config(text=text_translate)


tk_window = Tk()
tk_window.geometry("450x450")
tk_window.config(bg="light yellow")


lang_option = ["Hindi", "English", "Japanese", "Malayalam"]


entry_window = Entry(tk_window, bg="black", fg="white",
                     font=("Arial", 18, "bold"))
entry_window.place(x=20, y=40)


drop_down = StringVar()
drop_down.set("Select Language")  


list_lang = OptionMenu(tk_window, drop_down, *lang_option)
list_lang.config(bg="White", fg="black", font=("Arial", 16, "bold"))
list_lang.place(x=300, y=40)
t
two_label = Label(tk_window, text="\t\t\t\t\t", bg="white", fg="red", font=("Arial", 34, "bold"))
two_label.place(x=0, y=120)


two_label = Label(tk_window, text="Translated Text", bg="white", fg="red", font=("Arial", 16, "bold"))
two_label.place(x=180, y=140)

translate_b = Button(tk_window, text="Translate", bg="green", fg="white",
                     font=("Arial", 24, "bold"), command=translate_lang)
translate_b.place(x=220, y=220)

tk_window.mainloop()
