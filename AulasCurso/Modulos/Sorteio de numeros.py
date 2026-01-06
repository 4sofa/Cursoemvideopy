from random import randint

import tkinter as tk
from tkinter import messagebox


def converter():
    try:
        ninicial = int(entry_ninicial.get())
        nlimite = int(entry_nlimite.get())

        if ninicial <= 0 or nlimite <= 0:
            messagebox.showerror('Erro', 'Os valores devem ser positivos')
            return

        naleatorio = randint(ninicial, nlimite)
        label_result.config(text=f"Resultado sorteio: {naleatorio}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")


# Criação da janela principal

root = tk.Tk()

root.title("Sorteio")

# Criação dos widgets
label_ninicial = tk.Label(root, text="Insira um numero inicial: ")
label_ninicial.pack(pady=10)

entry_ninicial = tk.Entry(root)
entry_ninicial.pack(pady=5)

label_nlimite = tk.Label(root, text="Insira um limite: ")
label_nlimite.pack(pady=10)

entry_nlimite = tk.Entry(root)
entry_nlimite.pack(pady=5)

button_convert = tk.Button(root, text="Sortear", command=converter)
button_convert.pack(pady=10)

label_result = tk.Label(root, text="Resultado: ")
label_result.pack(pady=20)

# Execução da interface
root.mainloop()
