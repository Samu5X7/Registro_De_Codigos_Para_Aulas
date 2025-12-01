# [Bloco 1] =============== Imports =============== <title> Samuel <title/>

import requests as r
import customtkinter as ctk
from tkinter import messagebox as ms
import logging as log

log.basicConfig(
    filename="registro.log",
    encoding="utf-8",
    level=log.DEBUG,
    format="%(asctime)s :: %(levelname)s :: %(message)s"
)

# [Bloco 2] ================ funções ==============

def riquisicao():
    input_user.get()
    input_cep.get()

    try:
        url = f"https://brasilapi.com.br/api/cep/v1/{input_cep}"
    except ValueError as Valor:
        log.error("Erro", Valor)
    except TypeError: 
        log.error("Desconhecido Linha 26")

    try:
        resposta = r.get(url)
    
        if resposta.status_code == 200:
            rep = resposta.json()
            rua = rep['street']
            print(rua)
            log.info(f"{input_cep} :: {rua} :: {input_user}")
        else:
            print(input_cep)
            log.error("Erro", resposta.status_code)
    except:
        print("Erro aqui")

# [Bloco 3] =========== lógica ======== [Bloco 3]

# while True:
#     nome = input("Digite o nome de alguém para salvar a rua: ")

#     try:
#         cep = int(input("Digite o cep de pesquisa: "))
#         riquisicao(cep, nome)

#     except ValueError:
#         print("Valor inesperado, por gentileza Adicione um valor valido, ex: 12345678")
#         log.error("O valor não é um número")
#         cep = False
    
#     except TypeError:
#         log.warning("TypeError")
#         cep = False
    
#     except:
#         print("Deu erro")

#     else:
#         resposta = cep
#         print(resposta)
#     finally:
#         print("Excução terminada")

# [Bloco 3] =========== Tela Com verificação ======== [Bloco 3]

root = ctk.CTk()
root.geometry("500x300")

conteiner = ctk.CTkFrame(root,500,300)
conteiner.pack()

input_user = ctk.CTkEntry(conteiner, 100, placeholder_text="Digite user...")
input_user.pack_configure(pady=10)

input_cep = ctk.CTkEntry(conteiner, 100, placeholder_text="Digite algo cep...")
input_cep.pack()

button_confirmacao = ctk.CTkButton(conteiner,command=lambda:riquisicao())
button_confirmacao.pack_configure(pady=10)

root.mainloop()


        