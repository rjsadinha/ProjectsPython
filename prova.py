import tkinter as tk
import pyperclip

def limpar_cpf():
    cpf = entry_cpf.get()

    # Remove os pontos do CPF
    cpf_pontos = cpf.replace("-", ".")
    cpf_limpo = cpf_pontos.replace(".", "")

    # Copia o CPF limpo para a área de transferência
    pyperclip.copy(cpf_limpo)

    label_resultado['text'] = "CPF limpo copiado para a área de transferência:\n" + cpf_limpo

# Cria a janela
janela = tk.Tk()
janela.title("Limpar CPF")

# Cria os widgets da interface
label_cpf = tk.Label(janela, text="CPF com pontos:")
label_cpf.pack()

entry_cpf = tk.Entry(janela)
entry_cpf.pack()

button_limpar = tk.Button(janela, text="Limpar CPF", command=limpar_cpf)
button_limpar.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Inicia o loop de eventos da janela
janela.mainloop()