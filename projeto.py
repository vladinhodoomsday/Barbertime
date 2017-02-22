                                             #Interface#

from tkinter import *
import sqlite3
janela = Tk()
class Biblioteca(object):
	def __init__(self,janela):
                
                
		def login():
                        
			global fonte1,fonte2,lb,lb1,lb2,ed1,ed2,bt1,bt2
			fonte1 = ("Verdana","20","bold")
			fonte2 = ("Verdana","15","bold")
			self.lb = Label(janela,text="BARBEARIA",font=fonte2)
			self.lb1 = Label(janela,text="Usuário:",font=fonte2)
			self.lb2 = Label(janela,text="Senha:",font=fonte2)
			self.ed1 = Entry(janela,width=10,font=fonte2)
			self.ed2 = Entry(janela,width=10,font=fonte2,show="*")
			self.bt1 = Button(janela,text="Entrar",font=fonte2)
			self.bt2 = Button(janela,text="Cadastrar",font=fonte2,command=cadastrando)
			self.lb.grid(row=1,column=1)
			self.lb1.grid(row=2,column=0)
			self.lb2.grid(row=3,column=0)
			self.ed1.grid(row=2,column=1)
			self.ed2.grid(row=3,column=1)
			self.bt1.grid(row=4,column=0)
			self.bt2.grid(row=4,column=1)
		def cadastro():
			global fonte1,fonte2,lb,lb1,lb2,ed1,ed2,bt1,bt2,lb3
			self.lb = Label(janela,text="CADASTRO",font=fonte2)
			self.lb1 = Label(janela,text="Usuário:",font=fonte2)
			self.lb2 = Label(janela,text="Senha:",font=fonte2)
			self.ed1 = Entry(janela,width=10,font=fonte2)
			self.ed2 = Entry(janela,width=10,font=fonte2,show="*")
			self.lb3 = Label(janela,text="Idade:",font=fonte2)
			self.bt1 = Button(janela,text="Cadastrar",font=fonte2,command=banco_dados)
			self.bt2 = Button(janela,text="Voltar",font=fonte2,command=voltando)
			self.ed3 = Entry(janela,width=10,font=fonte2)
			self.lb.grid(row=1,column=1)
			self.lb1.grid(row=2,column=0)
			self.lb2.grid(row=3,column=0)
			self.ed1.grid(row=2,column=1)
			self.ed2.grid(row=3,column=1)
			self.bt1.grid(row=5,column=0)
			self.bt2.grid(row=5,column=1)
			self.lb3.grid(row=4,column=0)
			self.ed3.grid(row=4,column=1)
		def destruir_login():
			global fonte1,fonte2,lb,lb1,lb2,ed1,ed2,bt1,bt2
			self.lb.destroy()
			self.lb1.destroy()
			self.lb2.destroy()
			self.ed1.destroy()
			self.ed2.destroy()
			self.bt1.destroy()
			self.bt2.destroy()
		def destruir_cadastro():
			global fonte1,fonte2,lb,lb1,lb2,ed1,ed2,bt1,bt2,lb3,ed3
			self.lb.destroy()
			self.lb1.destroy()
			self.lb2.destroy()
			self.ed1.destroy()
			self.ed2.destroy()
			self.bt1.destroy()
			self.bt2.destroy()
			self.ed3.destroy()
			self.lb3.destroy()
			
		def cadastrando():

			destruir_login()
			cadastro()
		def voltando():
                        
			destruir_cadastro()
			login()
		def banco_dados():
			global fonte1,fonte2,lb,lb1,lb2,ed1,ed2,bt1,bt2,ed3,lb3
			conn = sqlite3.connect('cadastro.db')
			cursor = conn.cursor()
			usuario = self.ed1.get()
			senha = self.ed2.get()
			idade = self.ed3.get()
			cursor.execute("""INSERT INTO clientes (usuario,senha,idade)VALUES(?,?,?)""",(usuario,senha,idade))
			conn.commit()
			self.lb3 = Label(janela,text="Cliente cadastrado",font=("Verdana","13","bold"))
			self.lb3.grid(row=6,column=0)
			conn.close()
			
		












		login()
janela.resizable(False,False)
janela.title("BARBEARIA")
janela.geometry("+700+300")
Biblioteca(janela)
janela.mainloop()

                                        #Banco de dados#

import sqlite3

# conectando...
conn = sqlite3.connect('cadastro.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        
        senha     VARCHAR(11) NOT NULL,
        idade     VARCHAR(2) NOT NULL
       
        
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()