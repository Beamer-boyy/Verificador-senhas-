import re 
import tkinter as tk 
from tkinter import messagebox


#Verificacao de forca 
def verificar_forca(senha):
    pontuacao = 0

    #criterios
    if len(senha) >= 8:
        pontuacao += 1
    if re.search(r"[A-Z]", senha):
        pontuacao += 1 
    if re.search(r"[a-z]", senha):
        pontuacao += 1
    if re.search(r"[0-9]", senha):
        pontuacao += 1
    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>?,./]", senha):
        pontuacao += 1

    #Avaliacao da forca 
    if pontuacao <= 2:
        return "Fraca"
    elif pontuacao == 3 or pontuacao == 4:
        return "Media"
    else: 
        return "Forte"
    

def verificar():
        senha = entry.get()
        if not senha: 
            messagebox.showwarning("Digite uma senha!")
            return 
        resultado = verificar_forca(senha)
        messagebox.showinfo("Resultado", f"A força da senha é: {resultado}") 


#Criacao da interface 
janela = tk.Tk()
janela.title("Verificador de senha")
janela.geometry("300x150") 
janela.configure(bg="#1e1e2f")
janela.iconbitmap("cadeado.ico")

tk.Label(janela, text="Digite sua senha:", font=("Arial", 12, "bold"), bg="#1e1e2f", fg="white").pack(pady=10)
entry = tk.Entry(janela, width=30)
entry.pack()

tk.Button(janela, text="Verificar", command=verificar, bg="#4caf50", fg="white").pack(pady=10)

janela.mainloop()

        