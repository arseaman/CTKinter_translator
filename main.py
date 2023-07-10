from tkinter import END
from tkinter import *
import customtkinter as CTK
from googletrans import Translator
import langid

CTK.set_appearance_mode("dark")
TL = Translator()


class App(CTK.CTk):

    def detect_language(self, text):
        lang, confidence = langid.classify(text)
        return lang


    def get_input_text(self):
        text = self.input_field.get('1.0', END).strip()
        if self.detect_language(text) == 'ru':
            trans = TL.translate(text, dest='en')
        if self.detect_language(text) == 'en':
            trans = TL.translate(text, dest='ru')
        else:
            trans = TL.translate(text, dest='en')
        self.translate_field.delete('1.0', END)
        self.translate_field.insert('1.0', trans.text)

    def __init__(self):
        super().__init__()

        self.title("Translator")
        self.geometry("1200x900")
        self.iconbitmap('1.ico')
        # self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        self.button = CTK.CTkButton(self, font=('Arial', 22), text="Translate", command=self.get_input_text,
                                    border_color='white', anchor='center', width=1000, )
        self.button.grid(row=0, column=0, padx=20, pady=400, columnspan=2, sticky='ew')

        self.input_field = CTK.CTkTextbox(self, height=350, width=1100, wrap='word', font=('Arial', 22))
        self.input_field.grid(row=0, column=0, padx=20, pady=20, sticky='ewn', columnspan=2)

        self.translate_field = CTK.CTkTextbox(self, height=350, width=1100, wrap='word', font=('Arial', 22))
        self.translate_field.grid(row=0, column=0, padx=20, pady=10, sticky='ews', columnspan=2, rowspan=1)


app = App()
app.mainloop()
