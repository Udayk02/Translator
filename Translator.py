from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = Tk()
root.title('Translator')
root.geometry('530x330')
root.maxsize(530, 330)
root.minsize(530, 330)
root.iconbitmap('G:/C/translate.ico')

translate_label = Label(root, text='Translator', font=('Century Gothic', 20), )
translate_label.place(x=200, y=3)

# translate function


def translate():
    lang_1 = text1.get(1.0, 'end-1c')
    cl = choose_language.get()
    if text1.get(1.0, 'end-1c') == '':
        messagebox.showerror('Language Translator', 'Please enter some text')
    else:
        translator = Translator()
        op = translator.translate(lang_1, dest=cl)
        text2.insert(END, op.text)

# clear function


def clear():
    text1.delete(1.0, END)
    text2.delete(1.0, END)

# first drop down menu containing  auto detect


a = StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('Comic Sans', 10, 'bold'))
auto_detect['values'] = ('Auto Detect',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

# second drop down menu containing languages


lang = StringVar()
choose_language = ttk.Combobox(root, textvariable=lang, width=20, state='readonly', font=('Comic Sans', 10, 'bold'))
choose_language['values'] = (
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', ' Azerbaijani', 'Basque', 'Belarusian', 'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',)
choose_language.place(x=340, y=70)
choose_language.current(0)

# English text box
text1 = Text(root, width=30, height=10, borderwidth=5, relief=GROOVE)
text1.place(x=10, y=100)

# Translate text box
text2 = Text(root, width=30, height=10, borderwidth=5, relief=GROOVE)
text2.place(x=270, y=100)

# Translate button
translate = Button(root, text='Translate', font=('Century Gothic', 10), cursor='hand2', relief=RAISED, command=translate)
translate.place(x=100, y=280)

# Clear button
clear = Button(root, text='Clear', font=('Century Gothic', 10), cursor='hand2', relief=RAISED, command=clear)
clear.place(x=375, y=280)

# Exit Button
exit = Button(root, text='Exit', font=('Century Gothic', 10), cursor='hand2', relief=RAISED, command=root.quit)
exit.place(x=248, y=280)

root.mainloop()
