from tkinter import END, filedialog
from tkinter import *
import customtkinter as CTK
from googletrans import Translator
import langid
import easyocr


CTK.set_appearance_mode("dark")
TL = Translator()
reader = easyocr.Reader(['ru', 'en', 'uk'], gpu=False)


class App(CTK.CTk):

    def detect_language(self, text):
        lang, confidence = langid.classify(text)
        return lang

    def text_from_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            result = reader.readtext(file_path, detail=0, paragraph=True)
            self.translate_field.insert('1.0', result)

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
                                    border_color='white', anchor='center', width=500, )
        self.button.grid(row=0, column=0, padx=20, pady=400, columnspan=2, sticky='w')

        self.upload_button = CTK.CTkButton(self, font=('Arial', 22), text="+ Upload image", command=self.text_from_image,
                                    border_color='white', anchor='center', width=500, )
        self.upload_button.grid(row=0, column=1, padx=20, pady=400, columnspan=1, sticky='ew')

        self.input_field = CTK.CTkTextbox(self, height=350, width=1100, wrap='word', font=('Arial', 22))
        self.input_field.grid(row=0, column=0, padx=20, pady=20, sticky='ewn', columnspan=2)

        self.translate_field = CTK.CTkTextbox(self, height=350, width=1100, wrap='word', font=('Arial', 22))
        self.translate_field.grid(row=0, column=0, padx=20, pady=10, sticky='ews', columnspan=2, rowspan=1)


app = App()
app.mainloop()
