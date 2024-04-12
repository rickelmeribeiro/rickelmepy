import tkinter as tk
from tkinter import messagebox


def exibir_conteudo():
    nome = campo_nome.get()
    sobrenome = campo_sobrenome.get()
    print('Nome: ', nome)
    print('Sobrenome: ', sobrenome)

def exibir_mensagem_tkinter():
    messagebox.showinfo("Mensagem", "Parabéns, Deu Certo!")




# Criando uma janela com tkinter
janela_tkinter = tk.Tk()
janela_tkinter.title("Meu primeiro Formulário")
janela_tkinter.geometry("800x300")

#Criando botão com tkinter
botao_tkinter = tk.Button(janela_tkinter, text="Clique para mostrar uma mensagem", command=exibir_mensagem_tkinter)
botao_tkinter.pack()

#Criando label do input tkinter
label_nome = tk.Label(janela_tkinter, text="Nome:")
label_nome.pack()

#Criando o input tkinter
campo_nome = tk.Entry(janela_tkinter)
campo_nome.pack()

#Criando sobrenome label
label_sobrenome = tk.Label(janela_tkinter, text="Sobrenome:")
label_sobrenome.pack()

#Criando sobrenome tkinter
campo_sobrenome = tk.Entry(janela_tkinter)
campo_sobrenome.pack()


botao_exibir = tk.Button(janela_tkinter, text="Clique para exibir", command=exibir_conteudo)
botao_exibir.pack()










janela_tkinter.mainloop()
