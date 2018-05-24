from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import os


def main_window():
    window = Tk()

    window.update_idletasks()

    width = window.winfo_screenwidth()

    height = window.winfo_screenheight()

    x = (width - window.winfo_reqwidth()) / 2
    y = (height - window.winfo_reqheight()) / 2

    # print('Width: ' + str(window_width) + ' Height: ' + str(window_height))

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    window.title('Analizador de escritura a mano')

    menu_bar = Menu(window)

    # 'Archivo' pulldown menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Abrir', command=open_file)
    file_menu.add_command(label='Guardar', command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label='Salir', command=window.quit)
    menu_bar.add_cascade(label='Archivo', menu=file_menu)

    # 'Editar' pulldown menu
    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cortar", command=cut)
    edit_menu.add_command(label="Copiar", command=copy)
    edit_menu.add_command(label="Pegar", command=paste)
    menu_bar.add_cascade(label="Editar", menu=edit_menu)

    # 'Ayuda' pulldown menu
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Documentación", command=show_docs)
    help_menu.add_command(label="Acerca de", command=about)
    menu_bar.add_cascade(label="Ayuda", menu=help_menu)

    window.config(menu=menu_bar)

    window.minsize(500, 400)

    window.mainloop()


def open_file():
    from tkinter import filedialog
    file = filedialog.askopenfile()
    print(file)


def save_file():
    pass


def cut():
    pass


def copy():
    pass


def paste():
    pass


def show_docs():
    webbrowser.open_new_tab(r'https://github.com/NeshMx/handwriting-analysis')


def callback_git(event):
    webbrowser.open_new_tab(r'https://github.com/NeshMx')


def about():
    a = Toplevel()
    a.title('Acerca de')
    a.geometry('300x200')
    a.wm_attributes('-alpha', 0.7)
    image = Image.open('./icons/tmp_logo.png')
    image = image.resize((80, 80), Image.ANTIALIAS)
    image = image.convert('RGBA')
    logo = ImageTk.PhotoImage(image)
    logolbl = Label(a, image=logo)
    logolbl.pack()
    albl = Label(
        a, text='\nAnalizador de la escritura a mano\nPor: Alejandro Huerta Campos\nContacto:\nalex.huerta0424@hotmail.com')
    albl.pack()
    urlbl = Label(a, text='GitHub: NeshMx', fg='blue', cursor='hand2')
    urlbl.pack()
    urlbl.bind('<Button-1>', callback_git)
    a.mainloop()


def main():
    main_window()


if __name__ == '__main__':
    # if login.check_login() == True:
    #     main()
    # else:
    #     login.signup()
    main()
