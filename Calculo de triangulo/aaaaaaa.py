import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
root = tk.Tk()
root.title("Conversor de Celsius para Fahrenheit")

# Criação dos widgets
label_celsius = tk.Label(root, text="Temperatura em Celsius:")
label_celsius.pack(pady=10)

entry_celsius = tk.Entry(root)
entry_celsius.pack(pady=5)

button_convert = tk.Button(root, text="Converter", command=converter)
button_convert.pack(pady=10)

label_result = tk.Label(root, text="Resultado: ")
label_result.pack(pady=20)

# Execução da interface
root.mainloop()
