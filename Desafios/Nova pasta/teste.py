import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox as mbox

# ----------------- Dados ----------------- #
dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
matriz = [[] for _ in range(7)]  # 7 listas (uma por dia)

# ----------------- Funções ----------------- #
def indice_dia(nome_dia: str) -> int:
    """Converte nome do dia em índice (0..6)."""
    try:
        return dias_semana.index(nome_dia)
    except ValueError:
        return -1

def atualizar_lista():
    """Atualiza a Listbox com as tarefas do dia selecionado."""
    listbox_tarefas.delete(0, tk.END)
    idx = indice_dia(var_dia.get())
    if idx < 0:
        return
    for i, tarefa in enumerate(matriz[idx], start=1):
        listbox_tarefas.insert(tk.END, f"{i}. {tarefa}")

def adicionar():
    texto = entry_tarefa.get().strip()
    idx = indice_dia(var_dia.get())
    if idx < 0:
        mbox.showwarning("Dia inválido", "Selecione um dia da semana.")
        return
    if not texto:
        mbox.showwarning("Tarefa vazia", "Digite uma tarefa antes de adicionar.")
        return
    matriz[idx].append(texto)
    entry_tarefa.delete(0, tk.END)
    atualizar_lista()

def remover_selecionadas():
    idx = indice_dia(var_dia.get())
    if idx < 0:
        mbox.showwarning("Dia inválido", "Selecione um dia da semana.")
        return
    selecionadas = list(listbox_tarefas.curselection())
    if not selecionadas:
        mbox.showinfo("Remover", "Selecione ao menos uma tarefa para remover.")
        return
    # Remover de trás para frente para não bagunçar os índices
    for sel in reversed(selecionadas):
        del matriz[idx][sel]
    atualizar_lista()

def limpar_dia():
    idx = indice_dia(var_dia.get())
    if idx < 0:
        mbox.showwarning("Dia inválido", "Selecione um dia da semana.")
        return
    if not matriz[idx]:
        mbox.showinfo("Limpar dia", "Não há tarefas para limpar neste dia.")
        return
    if mbox.askyesno("Confirmar", f"Deseja limpar todas as tarefas de {dias_semana[idx]}?"):
        matriz[idx].clear()
        atualizar_lista()

def visualizar_semana():
    """Abre uma janela com a visão de todas as tarefas por dia."""
    top = ctk.CTkToplevel(app)
    top.title("Tarefas da semana")
    top.geometry("520x420")
    top.grab_set()

    texto = []
    for i, dia in enumerate(dias_semana):
        texto.append(f"{dia}:")
        if matriz[i]:
            for j, tarefa in enumerate(matriz[i], start=1):
                texto.append(f"  {j}. {tarefa}")
        else:
            texto.append("  — (sem tarefas)")
        texto.append("")  # linha em branco

    caixa = ctk.CTkTextbox(top, width=500, height=360)
    caixa.pack(padx=12, pady=(12, 8), fill="both", expand=True)
    caixa.insert("1.0", "\n".join(texto))
    caixa.configure(state="disabled")

    ctk.CTkButton(top, text="Fechar", command=top.destroy).pack(pady=(0, 12))

def trocar_dia(_event=None):
    atualizar_lista()

def adicionar_enter(_event=None):
    adicionar()

var1 = False  # controla o estado do tema

# função auxiliar para interpolar cores
def interpolar_cor(cor1, cor2, passo, total_passos):
    r1, g1, b1 = cor1
    r2, g2, b2 = cor2
    r = int(r1 + (r2 - r1) * (passo / total_passos))
    g = int(g1 + (g2 - g1) * (passo / total_passos))
    b = int(b1 + (b2 - b1) * (passo / total_passos))
    return f"#{r:02x}{g:02x}{b:02x}"

def animar_cor(btn, cor_inicio, cor_fim, passos=20, delay=30):
    for i in range(passos + 1):
        cor = interpolar_cor(cor_inicio, cor_fim, i, passos)
        btn.after(i * delay, lambda c=cor: btn.config(bg=c))

def mudar_tema(btn):
    global var1
    var1 = not var1
    
    if var1:
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        animar_cor(btn, (255, 255, 255), (0, 0, 0))  # branco → preto
        btn.config(fg="#FFFFFF")
    else:
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        animar_cor(btn, (0, 0, 0), (255, 255, 255))  # preto → branco
        btn.config(fg="#2C2525")


# ----------------- UI ----------------- #
ctk.set_appearance_mode("System")      # "Light", "Dark", "System"
ctk.set_default_color_theme("dark-blue")    # temas: "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Agendador de Tarefas (CTk)")
app.geometry("640x420")
app.minsize(560, 380)

# Frame principal
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=16, pady=16)

# Linha 1: Seleção do dia
linha1 = ctk.CTkFrame(frame)
linha1.pack(fill="x", pady=(0, 8))

ctk.CTkLabel(linha1, text="Dia:").pack(side="left", padx=(0, 8))
var_dia = tk.StringVar(value=dias_semana[1])  # padrão: Segunda
menu_dia = ctk.CTkOptionMenu(linha1, variable=var_dia, values=dias_semana, command=lambda *_: trocar_dia())
menu_dia.pack(side="left")

# Espaçador
ctk.CTkLabel(linha1, text="").pack(side="left", padx=12)

# Linha 2: Entrada de tarefa
linha2 = ctk.CTkFrame(frame)
linha2.pack(fill="x", pady=(0, 8))

ctk.CTkLabel(linha2, text="Tarefa:").pack(side="left", padx=(0, 8))
entry_tarefa = ctk.CTkEntry(linha2, placeholder_text="Ex.: Pegar avião na terça-feira ás 19:30.")
entry_tarefa.pack(side="left", fill="x", expand=True)
entry_tarefa.bind("<Return>", adicionar_enter)

btn_add = ctk.CTkButton(linha2, text="Adicionar", command=adicionar)
btn_add.pack(side="left", padx=(8, 0))

# Linha 3: Lista de tarefas (do dia selecionado)
linha3 = ctk.CTkFrame(frame)
linha3.pack(fill="both", expand=True, pady=(0, 8))

ctk.CTkLabel(linha3, text="Tarefas do dia").pack(anchor="w", pady=(0, 6))

# Usando Listbox padrão do Tk para seleção múltipla
listbox_tarefas = tk.Listbox(linha3, selectmode=tk.EXTENDED, height=10)
listbox_tarefas.pack(fill="both", expand=True, padx=2, pady=2)

# Linha 4: Botões de ação
linha4 = ctk.CTkFrame(frame)
linha4.pack(fill="x")

btn_remover = ctk.CTkButton(linha4, text="Remover selecionadas", command=remover_selecionadas)
btn_remover.pack(side="left",padx = 8)

btn_limpar = ctk.CTkButton(linha4, text="Apagar Tudo", command=limpar_dia)
btn_limpar.pack(side="left")

btn_tema = ctk.CTkButton(linha4, text="Mudar Tema", command=lambda:mudar_tema(listbox_tarefas)).pack(side="left",padx=8)

btn_visualizar = ctk.CTkButton(linha4, text="Visualizar semana", command=visualizar_semana)
btn_visualizar.pack(side="left")

# Inicializa lista com o dia padrão
atualizar_lista()

app.mainloop()