#this program translates words in the specified languages to english

from tkinter import *


def translate():
    word = Entry.get()
    lang = language.get()

    translation = dictionary.get(lang, {}).get(word)
    if translation:
        result_label.config(text="English Translation: " + translation)
    else:
        result_label.config(text="No translation found")


# dictionary with some words and transnlations
dictionary = {
    "tiv": {
     "ate": "father", "mbe": "mother", "iyor": "child", "aondo": "brother",
     "atema": "sister", "tsu": "water","sha": "drink","kuma": "farm","or":
     "house","ager": "farming","mkpakpa": "casssava","atuur": "yam","anongo":
     "goat","itsu": "sun","aza": "moon","vough": "leave","kwagh": "forest",
        "ver": "come", "ndeve": "good morning","sape": "goodnight",
    }
}
window = Tk()
window.title("Dictionary")

lan= ["tiv"]
language = StringVar(window)
language.set("Select Language")
lang_menu=OptionMenu(window,language,lan)
lang_menu.pack()
word_label = Label(window,text="EnterWord:")
word_label.pack()

entry = Entry(window)
entry.pack()

translate_button=Button(window,text="Translate",
       command=translate)
translate_button.pack()
result_label= Label(window,text="")
result_label.pack()
window.mainloop()
