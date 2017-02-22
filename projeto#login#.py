from tkinter import*
import sqlite3
def login():
    global fonte1,lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2   
    fonte1 = ("Arial","15","bold")
    lb = Label(janela,text="BARBEARIA",font=fonte1)
    lb1 = Label(janela,text="Usuário:",font=fonte1)
    lb2 = Label(janela,text="Senha:",font=fonte1)
    lb3 = Label(janela,text="Aguardando...",font=fonte1)
    lb3.grid(row=4,column=0,columnspan=2)
    ed1 = Entry(janela,width=10,font=fonte1)
    ed2  = Entry(janela,width=10,font=fonte1,show="*")
    bt1 = Button(janela,text="Entrar",font=fonte1,command=validando_conta)
    bt2 = Button(janela,text="Cadastrar",font=fonte1,command=cadastrar)
    lb.grid(row=0,column=0,columnspan=2)
    lb1.grid(row=1,column=0)
    lb2.grid(row=2,column=0)
    ed1.grid(row=1,column=1)
    ed2.grid(row=2,column=1)
    bt1.grid(row=3,column=0)
    bt2.grid(row=3,column=1)
def cadastro():
    global fonte1,lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2   
    fonte1 = ("Arial","15","bold")
    lb = Label(janela,text="CADASTRO BARBEARIA",font=fonte1)
    lb1 = Label(janela,text="Usuário:",font=fonte1)
    lb2 = Label(janela,text="Senha:",font=fonte1)
    lb3 = Label(janela,text="Aguardando...",font=fonte1)
    lb3.grid(row=4,column=0,columnspan=2)
    ed1 = Entry(janela,width=10,font=fonte1)
    ed2  = Entry(janela,width=10,font=fonte1,show="*")
    bt1 = Button(janela,text="Criar",font=fonte1,command=cadastrando_banco)
    bt2 = Button(janela,text="Voltar",font=fonte1,command=voltar)
    lb.grid(row=0,column=0,columnspan=2)
    lb1.grid(row=1,column=0)
    lb2.grid(row=2,column=0)
    ed1.grid(row=1,column=1)
    ed2.grid(row=2,column=1)
    bt1.grid(row=3,column=0)
    bt2.grid(row=3,column=1)
def destruindo():
    lb.destroy()
    lb1.destroy()
    lb2.destroy()
    lb3.destroy()
    ed1.destroy()
    ed2.destroy()
    bt1.destroy()
    bt2.destroy()
def cadastrar():
    destruindo()
    cadastro()
def voltar():
    destruindo()
    login()
def cadastrando_banco():
    lista = []
    global lb3,fonte1,ed1,ed2
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    usuario = ed1.get()
    senha = ed2.get()
    lista.append(usuario)
    lista.append(senha)
    if "" in lista:
        lb3 = Label(janela,text="Informe todos os valores",font=fonte1,fg="red")
        lb3.grid(row=4,column=0,columnspan=2)
        
    else:
        cursor.execute("INSERT INTO clientes (usuario,senha)VALUES(?,?)",(usuario,senha))
        lb3.destroy()
        lb3 = Label(janela,text="Cliente cadastrado",font=fonte1,fg="green")
        lb3.grid(row=4,column=0,columnspan=2)
        conn.commit()
        conn.close()
def validando_conta():
    global ed1,ed2,lb3,fonte1,janela
    lista = []
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    usuario = ed1.get()
    senha = ed2.get()
    lista.append(usuario)
    lista.append(senha)
    if "" in lista:
        lb3 = Label(janela,text="Informe todos os valores",font=fonte1,fg="red")
        lb3.grid(row=4,column=0,columnspan=2)
    else:
        cursor.execute("""SELECT usuario,senha FROM clientes;""")
        for linha in cursor.fetchall():
            if usuario in linha:
                if senha in linha:
                    lista.append(0)
            else:
                lista.append(1)
        if 0 in lista:
            janela.destroy()
            import agendamento
        else:
            lb3.destroy()
            lb3 = Label(janela,text="Conta inválida",font=fonte1,fg="red")
            lb3.grid(row=4,column=0,columnspan=2)
            
global fonte1,lb,lb1,lb2,lb3,ed1,ed2,bt1,bt2   
janela = Tk()
fonte1 = ("Arial","15","bold")
lb = Label(janela,text="BARBEARIA",font=fonte1)
lb1 = Label(janela,text="Usuário:",font=fonte1)
lb2 = Label(janela,text="Senha:",font=fonte1)
lb3 = Label(janela,text="Aguardando...",font=fonte1)
lb3.grid(row=4,column=0,columnspan=2)
ed1 = Entry(janela,width=10,font=fonte1)
ed2  = Entry(janela,width=10,font=fonte1,show="*")
bt1 = Button(janela,text="Entrar",font=fonte1,command=validando_conta)
bt2 = Button(janela,text="Cadastrar",font=fonte1,command=cadastrar)
lb.grid(row=0,column=0,columnspan=2)
lb1.grid(row=1,column=0)
lb2.grid(row=2,column=0)
ed1.grid(row=1,column=1)
ed2.grid(row=2,column=1)
bt1.grid(row=3,column=0)
bt2.grid(row=3,column=1)
janela.title("Barbearia")
janela.geometry("+600+300")
janela["bg"]= "pink"
janela.mainloop()