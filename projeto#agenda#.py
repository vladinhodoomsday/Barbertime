from tkinter import*
import sqlite3
janela = Tk()

def tela_principal():
    global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox
    fonte = ("Arial","15","bold")
    lb = Label(janela,text="AGENDAMENTO",font=fonte)
    nome = Label(janela,text="Nome:",font=fonte)
    nome2 = Entry(janela,font=fonte)
    lb1 = Label(janela,text="Horário:",font=fonte)
    lb2 = Label(janela,text="Data:",font=fonte)
    ed1 = Entry(janela,textvariable =IntVar,font=fonte)
    ed2  = Entry(janela,textvariable= IntVar,font=fonte)
    lb3  = Label(janela,text="Aguardando...",font=fonte)
    bt1 = Button(janela,text="Agendar",font=fonte,command=agendar)
    bt2 = Button(janela,text="Ver Reservas",font=fonte,command=ver_reservas)
    

    lb.grid(row=0,column=0,columnspan=2)
    nome.grid(row=1,column=0)
    nome2.grid(row=1,column=1)
    lb1.grid(row=2,column=0)
    lb2.grid(row=3,column=0)
    ed1.grid(row=2,column=1)
    ed2.grid(row=3,column=1)
    bt1.grid(row=4,column=0)
    bt2.grid(row=4,column=1)
    lb3.grid(row=5,column=0,columnspan=2)
    
    janela.title("Agendamento Barbearia")

def agendar():
    global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox
    
    lista = []
    
    conn  = sqlite3.connect("agendamento.db")
    cursor = conn.cursor()
    nome_cliente = nome2.get()
    horario = ed1.get()
    data = ed2.get()
    lista.append(nome)
    lista.append(horario)
    lista.append(data)
    if "" in lista:
        lb3 = Label(janela,text="Informe todos os valores",font=fonte,fg="red")
        lb3.grid(row=5,column=0,columnspan=2)
    
    
    else:
        cursor.execute("INSERT INTO clientes(nome,horario,data) VALUES(?,?,?)",(nome_cliente,horario,data))
        lb3.destroy()
        lb3 = Label(janela,text="Reservado com sucesso!",font=fonte,fg="green")
        lb3.grid(row=5,column=0,columnspan=2)
        conn.commit()
        conn.close()
        

def destruindo_agendamento():
    global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox,bt3
    lb.destroy()
    lb1.destroy()
    lb2.destroy()
    ed1.destroy()
    ed2.destroy()
    lb3.destroy()
    bt1.destroy()
    bt2.destroy()
    nome.destroy()
    nome2.destroy()
    bt3.destroy()
def ver_reservas():
    global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox
    global fonte
    lb3.destroy()
    destruindo_agendamento()
    conn  = sqlite3.connect("agendamento.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome,horario,data FROM clientes;")
    lb = Label(janela,text="RESERVAS",font=fonte)
    lb.grid(row=0,column=0)
    bt = Button(janela,text="Voltar",font=fonte,command=voltar)
    bt.grid(row=0,column=1)
    listabox = Listbox(janela,height=20,width=100)
    listabox.grid(row=1,column=0)
    for linha in cursor.fetchall():
        listabox.insert(END,("NOME:",linha[0],"HORÁRIO:",linha[1],"DATA:",linha[2]))
        
  
        
       
        
        
        
def destruindo_reservas():
    global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox
    lb.destroy()
    bt.destroy()
    listabox.destroy()
    
def voltar():
    global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox
    destruindo_reservas()
    
    
    tela_principal()
    
def sair():
    janela.destroy()
    import login
    
        
    
    
        
global lb,nome,nome2,lb1,lb2,ed1,ed2,lb3,bt1,bt2,lb,bt,listabox       
fonte = ("Arial","15","bold")
lb = Label(janela,text="AGENDAMENTO",font=fonte)
nome = Label(janela,text="Nome:",font=fonte)
nome2 = Entry(janela,font=fonte)
lb1 = Label(janela,text="Horário:",font=fonte)
lb2 = Label(janela,text="Data:",font=fonte)
ed1 = Entry(janela,font=fonte)
ed2  = Entry(janela,font=fonte)
lb3  = Label(janela,text="Aguardando...",font=fonte)
bt1 = Button(janela,text="Agendar",font=fonte,command=agendar)
bt2 = Button(janela,text="Ver Reservas",font=fonte,command=ver_reservas)
bt3 = Button(janela,text="Sair",font=fonte,command=sair)
bt3.grid(row=4,column=2)
lb.grid(row=0,column=0,columnspan=2)
nome.grid(row=1,column=0)
nome2.grid(row=1,column=1)
lb1.grid(row=2,column=0)
lb2.grid(row=3,column=0)
ed1.grid(row=2,column=1)
ed2.grid(row=3,column=1)
bt1.grid(row=4,column=0)
bt2.grid(row=4,column=1)
lb3.grid(row=5,column=0,columnspan=2)
janela.title("Agendamento Barbearia")
janela.geometry("+600+300")
janela["bg"]="pink"
janela.mainloop()
