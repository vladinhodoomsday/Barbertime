from tkinter import*
def semana ():
    global nome
    nome= str(input("digite o nome do cliente aqui pra que ele possa se cadastrar:"))
    print(nome, "esta cadastrado em nosso sistema")
    global semana
    semana = str(input("coloque aqui a semana que o cliente quer deseja ser atendido s1,s2,s3,s4: "))
    global dia
    dia = str(input("qual o dia da semana q vc deseja ser atendido de: "))
    if semana=="s1" and dia=="segunda":
        d1= float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30,11:35/12:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d1, "horas de segunda feira")
    elif semana=="s1" and dia=="terça":
        d2=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d2, "horas de terça feira")
    elif semana=="s1" and dia=="quarta":
        d3=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d3, "horas de quarta feira")
    elif semana=="s1" and dia=="quinta":
        d4=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d4, "horas de quinta feria")
    elif semana=="s1" and dia=="sexta":
        d5=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d5, "horas de sexta feira")
    elif semana=="s1" and dia=="sabado":
        d6=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 16:55/17:25, 17:30/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d6, "horas de sabado")
    elif semana=="s1" and dia=="domingo":
        d7=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15"))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d7, "horas de domingo")                   

    elif semana=="s2" and dia=="segunda":
        d1= float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30,11:35/12:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d1, "horas")
    elif semana=="s2" and dia=="terça":
        d2=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d2, "horas")
    elif semana=="s2" and dia=="quarta":
        d3=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d3, "horas")
    elif semana=="s2" and dia=="quinta":
        d4=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d4, "horas")
    elif semana=="s2" and dia=="sexta":
        d5=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d5, "horas")
    elif semana=="s2" and dia=="sabado":
        d6=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 16:55/17:25, 17:30/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d6, "horas")
    elif semana=="s2" and dia=="domingo":
        d7=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15"))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d7, "horas")                   

    elif semana=="s3" and dia=="segunda":
        d1= float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30,11:35/12:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d1, "horas")
    elif semana=="s3" and dia=="terça":
        d2=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d2, "horas")
    elif semana=="s3" and dia=="quarta":
        d3=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d3, "horas")
    elif semana=="s3" and dia=="quinta":
        d4=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d4, "horas")
    elif semana=="s3" and dia=="sexta":
        d5=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d5, "horas")
    elif semana=="s3" and dia=="sabado":
        d6=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 16:55/17:25, 17:30/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d6, "horas")
    elif semana=="s3" and dia=="domingo":
        d7=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15"))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d7, "horas")
        
    elif semana=="s4" and dia=="segunda":
        d1= float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30,11:35/12:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d1, "horas")
    elif semana=="s4" and dia=="terça":
        d2=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d2, "horas")
    elif semana=="s4" and dia=="quarta":
        d3=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d3, "horas")
    elif semana=="s4" and dia=="quinta":
        d4=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d4, "horas")
    elif semana=="s4" and dia=="sexta":
        d5=float(input("apartir de qual a hora q o cliente deseja ser atendido : 8:00/8:30, 8:35/9:05, 9:10/9:40, 9:45/10:15, 10:20/10:50, 11:00/11:30, 11:35/12:00, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 17:00/17:30, 17:35/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d5, "horas")
    elif semana=="s4" and dia=="sabado":
        d6=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15, 14:00/14:30, 14:35/15:05, 15:10/15:40, 15:45/16:15, 16:20/16:50, 16:55/17:25, 17:30/18:00 "))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d6, "horas")
    elif semana=="s4" and dia=="domingo":
        d7=float(input("apartir de qual a hora q o cliente deseja ser atendido : 7:00/7:30, 7:35/8:05, 8:10/8:40, 8:45/9:15, 9:20/9:50, 10:00/10:30, 10:35/11:05, 11:10/11:40, 11:45/12:15"))
        print("o cliente:",nome,"esta com serviço marcado para apartir de:", d7, "horas")  
janela= Tk()
bt= Button(janela,width=20, text="clique para se cadastrar", command=semana )
bt.place(x=100, y=100)
janela.geometry("300x300+150+150")
janela.mainloop()