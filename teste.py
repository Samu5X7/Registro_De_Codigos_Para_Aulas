import customtkinter as ctk
import tkinter.messagebox as msg

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("System")  # "Light" ou "Dark"
ctk.set_default_color_theme("blue")

# Função para capturar o valor do Entry
def mostrar_valor():
    valor = entrada.get()  # Pega o texto digitado
    if valor.strip() == "":
        msg.showwarning("Aviso", "O campo está vazio!")
    else:
        msg.showinfo("Valor Capturado", f"Você digitou: {valor}")

# Criando a janela principal
janela = ctk.CTk()
janela.title("Exemplo Entry CTk")
janela.geometry("300x150")

# Criando um Entry
entrada = ctk.CTkEntry(janela, placeholder_text="Digite algo...")
entrada.pack(pady=10)

# Botão para puxar o valor
botao = ctk.CTkButton(janela, text="Puxar Valor", command=mostrar_valor)
botao.pack(pady=10)

# Loop principal
janela.mainloop()
