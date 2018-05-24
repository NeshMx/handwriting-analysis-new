import tkinter as tk
import os


class Analyzer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # self.title('Analizador de escritura a mano')
        # self.iconphoto(r'./icons/tmp_logo.png')
        self._frame = None
        self.switch_frame(Login)

    def switch_frame(self, frame_class):
        '''Destroy current frame and replaces it with a new one'''
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        # self._frame.pack()


class Login(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        master.title('Registro')
        self.creds = 'creds.tmp'
        if os.path.isfile(self.creds):
            self.login()
        else:
            self.signup()

    def signup(self):
        global name_e
        global password_e

        instruction = tk.Label(
            self.master, text='Por favor, introduce nuevas credenciales\n')
        instruction.grid(row=0, column=0, sticky='e')

        name_l = tk.Label(self.master, text='Nuevo usuario: ')
        password_l = tk.Label(self.master, text='Nueva contrasena: ')
        name_l.grid(row=1, column=0, sticky='w')
        password_l.grid(row=2, column=0, sticky='w')

        name_e = tk.Entry(self.master)
        password_e = tk.Entry(self.master, show='*')
        name_e.grid(row=1, column=1)
        password_e.grid(row=2, column=1)

        signup_button = tk.Button(
            self.master, text='Registrarse', command=self.fs_signup)
        signup_button.grid(columnspan=2, sticky='w')

    def fs_signup(self):
        with open(self.creds, 'w') as f:
            f.write(name_e.get())
            f.write('\n')
            f.write(password_e.get())
            f.close()        
        # self.master.destroy()
        self.login()

    def login(self):
        global name_el
        global password_el

        instruction = tk.Label(self.master, text='Por favor, inicia sesion\n')
        instruction.grid(sticky='e')

        name_l = tk.Label(self.master, text='Nombre de usuario: ')
        password_l = tk.Label(self.master, text='Contrasena: ')
        name_l.grid(row=1, sticky='w')
        password_l.grid(row=2, sticky='w')

        name_el = tk.Entry(self.master)
        password_el = tk.Entry(self.master, show='*')
        name_el.grid(row=1, column=1)
        password_el.grid(row=2, column=1)

        login_button = tk.Button(self.master, text='Login', command=self.check_login)
        # val = login_button.
        # print(val)
        login_button.grid(columnspan=2, sticky='w')

        rm_user = tk.Button(self.master, text='Eliminar usuario',
                            fg='red', command=self.del_user)
        rm_user.grid(columnspan=2, sticky='w')

    def check_login(self):
        with open(self.creds) as f:
            data = f.readlines()
            user = data[0].rstrip()
            passw = data[1].rstrip()
        if name_el.get() == user and password_el.get() == passw:
            rlbl = tk.Label(self.master, text='\n[+] Conectado')
            rlbl.grid(row=0, column=0, sticky='e')
            # rlbl.destroy()
        else:
            rlbl = tk.Label(self.master, text='[!] Login no valido')
            rlbl.grid(row=0, column=0, sticky='e')
            # rlbl.destroy()

    def del_user(self):
        os.remove(self.creds)
        self.destroy()
        self.signup()

# class Main(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         master.title('Analizador de escritura a mano')


if __name__ == '__main__':
    app = Analyzer()
    app.mainloop()
