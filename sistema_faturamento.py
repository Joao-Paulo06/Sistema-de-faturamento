from tkinter import messagebox
import customtkinter as ctk
ctk.set_appearance_mode("dark")


def faturamento():
    # Lógica para lidar com a parte de faturamento
    pass

def estoque():
    # Lógica para lidar com a parte de estoque
    pass

def financeiro():
    # Lógica para lidar com a parte financeira
    pass

def customizacao():
    # Lógica para lidar com a customização
    pass

def configuracoes():
    # Lógica para lidar com as configurações
    pass

def ajuda():
    # Lógica para lidar com a ajuda
    pass

def sair():
    janela.quit()
    
    
def verificar_login():
    if entry_usuario.get() == "usuario" and entry_senha.get() == "senha":
        abrir_segunda_janela()
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha estão incorretos!")
        
        
def abrir_segunda_janela():
    janela.withdraw()
    segunda_janela = ctk.CTkToplevel(janela)
    segunda_janela.geometry("1280x720")
    segunda_janela.title("Segunda Janela")
    segunda_janela.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    btn_faturamento = ctk.CTkButton(segunda_janela, text="Faturamento", command=faturamento)
    btn_faturamento.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    btn_estoque = ctk.CTkButton(segunda_janela, text="Estoque", command=estoque)
    btn_estoque.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    btn_financeiro = ctk.CTkButton(segunda_janela, text="Financeiro", command=financeiro)
    btn_financeiro.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    btn_customizacao = ctk.CTkButton(segunda_janela, text="Customização", command=customizacao)
    btn_customizacao.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    btn_configuracoes = ctk.CTkButton(segunda_janela, text="Configurações", command=configuracoes)
    btn_configuracoes.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

    btn_ajuda = ctk.CTkButton(segunda_janela, text="Ajuda", command=ajuda)
    btn_ajuda.grid(row=0, column=5, padx=5, pady=5, sticky="ew")

    btn_sair = ctk.CTkButton(segunda_janela, text="Sair", command=sair)
    btn_sair.grid(row=0, column=6, padx=5, pady=5, sticky="ew")
    
    
janela = ctk.CTk()
janela.title("Tela de Login")
janela.geometry("1280x720")

ctk.CTkLabel(janela, text="Nome de usuário:").pack(padx=10, pady=10)
entry_usuario = ctk.CTkEntry(janela)
entry_usuario.pack(padx=10, pady=10)

ctk.CTkLabel(janela, text="Senha:").pack()
entry_senha = ctk.CTkEntry(janela, show="*")
entry_senha.pack(padx=10, pady=10)
ctk.CTkButton(janela, text="Login", command=verificar_login).pack(padx=10, pady=10)


janela.mainloop()