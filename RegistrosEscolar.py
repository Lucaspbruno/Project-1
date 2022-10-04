from tkinter import *

class Aluno:

    def __init__(self, nome, matricula, turma):
        self.nome = nome
        self.matricula = matricula
        self.turma = turma

    def getNome(self):
        print("Meu nome é "+self.nome)

listaDeAlunos = []

def atualizaBD():
    arquivo = open("bdAlunos.txt","w")
    arquivo.close()
    for x in listaDeAlunos:
        arquivo = open("bdAlunos.txt","a")
        arquivo.write(x.nome+"#"+x.matricula+"#"+x.turma+"\n")
        arquivo.close()

def atualizaLista():
    listaDeAlunosLB.delete(0,END)
    for x in listaDeAlunos:
        listaDeAlunosLB.insert("end",x.nome)
    atualizaBD()


def registrar():
    a = Aluno(nomeE.get(), matriculaE.get(), turmaE.get())
    repetida = FALSE
    for x in listaDeAlunos:
        if x.matricula == a.matricula:
            matriculaE.delete(0, 'end')
            turmaE.delete(0, 'end')
            nomeE.delete(0, 'end')
            
            logL.configure(text="Aluno Repetido!")
            repetida = True
    if repetida == FALSE:        
        listaDeAlunos.append(a)
        nomeE.delete(0, 'end')
        matriculaE.delete(0, 'end')
        turmaE.delete(0, 'end')
        logL.configure(text="Log: Aluno Registrado com Sucesso!")
        atualizaLista()

    
def pesquisar():
    m = matriculaE.get()
    NaoAchou = True
    nomeE.delete(0, 'end')
    turmaE.delete(0, 'end')
    for x in listaDeAlunos:
        if x.matricula == m:
            nomeE.insert(0,x.nome)
            turmaE.insert(0,x.turma)
            logL.configure(text="Log: Aluno Encontrado com Sucesso!")
            NaoAchou = False                

    if(NaoAchou):
            logL.configure(text="Log: Aluno Não Encontrado!")

        



            
def apagar():
    m = matriculaE.get()
    NaoAchou = True
    for x in listaDeAlunos:
        if x.matricula == m:
            matriculaE.delete(0, 'end')
            turmaE.delete(0, 'end')
            nomeE.delete(0, 'end')
            listaDeAlunos.remove(x)
            logL.configure(text="Log: Aluno Removido com Sucesso!")
            NaoAchou = False
    
    if(NaoAchou):
            logL.configure(text="Log: Aluno Não Encontrado!")
    atualizaLista()
    

def atualizar():
    m = matriculaE.get()
    NaoAchou = True
    for x in listaDeAlunos:
        if x.matricula == m:
            listaDeAlunos.remove(x)
            x.nome = nomeE.get()
            x.turma = turmaE.get()
            listaDeAlunos.append(x)
            matriculaE.delete(0, 'end')
            turmaE.delete(0, 'end')
            nomeE.delete(0, 'end')
            logL.configure(text="Log: Aluno Atualizado com Sucesso!")
            NaoAchou = False

    if(NaoAchou):
            logL.configure(text="Log: Aluno Não Encontrado!")
    atualizaLista()

def limpar():
    matriculaE.delete(0, 'end')
    turmaE.delete(0, 'end')
    nomeE.delete(0, 'end')
    logL.configure(text="Log: Campos limpos")


def showSelected(event):
    nome = listaDeAlunosLB.get(listaDeAlunosLB.curselection())
    nomeE.delete(0,'end')
    matriculaE.delete(0,'end')
    turmaE.delete(0,'end')
    nomeE.insert(0,nome)
    for x in listaDeAlunos:
        if x.nome == nome:
            matriculaE.insert(0,x.matricula)
            turmaE.insert(0,x.turma)
    listaDeAlunosLB.select_clear(listaDeAlunosLB.curselection())

def puxarBD():
    arquivo = open("bdAlunos.txt", "r")
    for linha in arquivo:
        if "#" in linha:
            nome = linha.split("#")[0]
            matricula = linha.split("#")[1]
            turma = linha.split("#")[2]
            x = Aluno(nome, matricula, turma)
            listaDeAlunos.append(x)
    arquivo.close()
    atualizaLista()        
    

janela = Tk()

janela.title("Escola raio de Luz")
janela.geometry("500x400")

topo = Frame(janela)
topo.pack(side=TOP)

baixo = Frame(janela)
baixo.pack(side=BOTTOM)

baixoEsquerda = Frame(baixo)
baixoEsquerda.pack(side=LEFT)

baixoDireita = Frame(baixo)
baixoDireita.pack(side=RIGHT)

esquerda = Frame(topo)
esquerda.pack(side=LEFT)

centro = Frame(topo)
centro.pack(side=LEFT)

direita = Frame(topo)
direita.pack(side=RIGHT)


nomeL = Label(esquerda, text="Nome: ")

matriculaL = Label(esquerda, text="Matricula: ")

turmaL = Label(esquerda, text="Turma: ")

nomeE = Entry(centro)
matriculaE = Entry(centro)
turmaE = Entry(centro)

botaoRegistrar = Button(direita, text="REGISTRAR", command=registrar)
botaoAtualizar = Button(direita, text="ATUALIZAR", command=atualizar)
botaoPesquisar = Button(direita, text="PESQUISAR", command=pesquisar)
botaoApagar = Button(direita, text="APAGAR", command=apagar)
botaoLimpar = Button(direita, text="LIMPAR", command=limpar)

logL = Label(baixoEsquerda, text="LOG: ")
listaDeAlunosL = Label(baixoDireita, text="Lista de Alunos:")
listaDeAlunosLB = Listbox(baixoDireita)
listaDeAlunosLB.bind('<<ListboxSelect>>', showSelected)


nomeL.pack(padx=10,pady=10)
nomeE.pack(padx=10,pady=10)
matriculaL.pack(padx=10,pady=10)
matriculaE.pack(padx=10,pady=10)
turmaL.pack(padx=10,pady=10)
turmaE.pack(padx=10,pady=10)
botaoLimpar.pack(padx=10,pady=0)

botaoRegistrar.pack(padx=100,pady=20)
botaoAtualizar.pack(padx=100,pady=20)
botaoPesquisar.pack(padx=100,pady=20)
botaoApagar.pack(padx=100,pady=20)
logL.pack(padx=50,pady=20)
listaDeAlunosL.pack()
listaDeAlunosLB.pack()

puxarBD()

janela.mainloop()
