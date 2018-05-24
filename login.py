from tkinter import *
import os

creds = 'tempfile.temp'

# value = 0
# def get_value():
#     global value
#     value = True


def signup():
    global name_e
    global password_e
    global roots

    roots = Tk()
    roots.title('Registro')
    instruction = Label(
        roots, text='Por favor, introduce nuevas credenciales\n')
    instruction.grid(row=0, column=0, sticky=E)

    name_l = Label(roots, text='Nuevo usuario: ')
    password_l = Label(roots, text='Nueva contrasena: ')
    name_l.grid(row=1, column=0, sticky=W)
    password_l.grid(row=2, column=0, sticky=W)

    name_e = Entry(roots)
    password_e = Entry(roots, show='*')
    name_e.grid(row=1, column=1)
    password_e.grid(row=2, column=1)

    signup_button = Button(roots, text='Registrarse', command=fs_signup)
    signup_button.grid(columnspan=2, sticky=W)

    roots.mainloop()


def fs_signup():
    with open(creds, 'w') as f:
        f.write(name_e.get())
        f.write('\n')
        f.write(password_e.get())
        f.close()

    roots.destroy()
    login()


def login():
    global name_el
    global password_el
    global root_a

    root_a = Tk()
    root_a.title('Login')

    instruction = Label(root_a, text='Por favor, inicia sesion\n')
    instruction.grid(sticky=E)

    name_l = Label(root_a, text='Nombre de usuario: ')
    password_l = Label(root_a, text='Contrasena: ')
    name_l.grid(row=1, sticky=W)
    password_l.grid(row=2, sticky=W)

    name_el = Entry(root_a)
    password_el = Entry(root_a, show='*')
    name_el.grid(row=1, column=1)
    password_el.grid(row=2, column=1)

    login_button = Button(root_a, text='Login', command=check_login)
    # val = login_button.
    # print(val)
    login_button.grid(columnspan=2, sticky=W)

    rm_user = Button(root_a, text='Eliminar usuario',
                     fg='red', command=del_user)
    rm_user.grid(columnspan=2, sticky=W)

    root_a.mainloop()


def check_login():
    with open(creds) as f:
        data = f.readlines()
        user = data[0].rstrip()
        passw = data[1].rstrip()
    if name_el.get() == user and password_el.get() == passw:
        r = Tk()
        r.title('Bienvenido')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[+] Conectado')
        rlbl.pack()
        r.mainloop()
        rlbl.destroy()
    else:
        r = Tk()
        r.title('Error')
        r.geometry('150x50')
        rlbl = Label(r, text='[!] Login no valido')
        rlbl.pack()
        r.mainloop()
        rlbl.destroy()


def del_user():
    os.remove(creds)
    root_a.destroy()
    signup()


if os.path.isfile(creds):
    login()
else:
    signup()
