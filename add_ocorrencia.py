import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
from datetime import datetime

def apply_date_mask(event):
    value = data_var.get()
    value = re.sub(r'[^0-9]', '', value)  # Remove qualquer caractere não numérico
    if len(value) > 2:
        value = value[:2] + '/' + value[2:]
    if len(value) > 5:
        value = value[:5] + '/' + value[5:]
    data_var.set(value)
    # Move o cursor para o final do campo de entrada
    data_entry.icursor(tk.END)

def validate_date(date):
    """Valida se a data está no formato DD/MM/YYYY e é uma data válida."""
    if not re.match(r'\d{2}/\d{2}/\d{4}', date):
        return False
    day, month, year = map(int, date.split('/'))
    if not (1 <= day <= 31 and 1 <= month <= 12):
        return False
    if month == 2 and day > 29:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    return True

def convert_date_format(date):
    """Converte a data de DD/MM/YYYY para YYYY-MM-DD."""
    try:
        day, month, year = map(int, date.split('/'))
        return datetime(year, month, day).strftime('%Y-%m-%d')
    except ValueError:
        return None

def add_ocorrencia():
    data = data_var.get()
    hora = hora_var.get()
    posto = posto_var.get()
    topicos_id = topicos_id_var.get()
    nome_salva_vidas = nome_salva_vidas_var.get()
    nome_vitima = nome_vitima_var.get()
    grau = grau_var.get()
    sexo = sexo_var.get()
    idade = idade_var.get()
    estado_civil = estado_civil_var.get()
    profissao = profissao_var.get()
    cidade = cidade_var.get()
    uf = uf_var.get()
    endereco = endereco_var.get()
    turista = turista_var.get()
    observacao = observacao_var.get()

    if not validate_date(data):
        messagebox.showerror("Erro", "Data inválida. Use o formato DD/MM/YYYY.")
        return

    formatted_date = convert_date_format(data)
    if formatted_date is None:
        messagebox.showerror("Erro", "Data inválida. Não foi possível converter.")
        return

    conn = sqlite3.connect('registro_ocorrencia.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ocorrencias (data, hora, posto, topicos_id, nome_salva_vidas, nome_vitima, grau, sexo, idade, estado_civil, profissao, cidade, uf, endereco, turista, observacao)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (formatted_date, hora, posto, topicos_id, nome_salva_vidas, nome_vitima, grau, sexo, idade, estado_civil, profissao, cidade, uf, endereco, turista, observacao))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Ocorrência adicionada com sucesso!")
    root.destroy()

root = tk.Tk()
root.title("Adicionar Nova Ocorrência")

# Variáveis
data_var = tk.StringVar()
hora_var = tk.StringVar()
posto_var = tk.StringVar()
topicos_id_var = tk.StringVar()
nome_salva_vidas_var = tk.StringVar()
nome_vitima_var = tk.StringVar()
grau_var = tk.StringVar()
sexo_var = tk.StringVar()
idade_var = tk.StringVar()
estado_civil_var = tk.StringVar()
profissao_var = tk.StringVar()
cidade_var = tk.StringVar()
uf_var = tk.StringVar()
endereco_var = tk.StringVar()
turista_var = tk.StringVar()
observacao_var = tk.StringVar()

# Campos de Entrada
tk.Label(root, text="Data (DD/MM/YYYY):").grid(row=0, column=0, sticky='e')
data_entry = tk.Entry(root, textvariable=data_var)
data_entry.grid(row=0, column=1)

# Aplicar máscara na entrada de dados
data_entry.bind('<KeyRelease>', apply_date_mask)

tk.Label(root, text="Hora:").grid(row=1, column=0, sticky='e')
tk.Entry(root, textvariable=hora_var).grid(row=1, column=1)
tk.Label(root, text="Posto:").grid(row=2, column=0, sticky='e')
tk.Entry(root, textvariable=posto_var).grid(row=2, column=1)
tk.Label(root, text="ID do Tópico:").grid(row=3, column=0, sticky='e')
tk.Entry(root, textvariable=topicos_id_var).grid(row=3, column=1)
tk.Label(root, text="Nome do Salva-Vidas:").grid(row=4, column=0, sticky='e')
tk.Entry(root, textvariable=nome_salva_vidas_var).grid(row=4, column=1)
tk.Label(root, text="Nome da Vítima:").grid(row=5, column=0, sticky='e')
tk.Entry(root, textvariable=nome_vitima_var).grid(row=5, column=1)
tk.Label(root, text="Grau:").grid(row=6, column=0, sticky='e')
tk.Entry(root, textvariable=grau_var).grid(row=6, column=1)
tk.Label(root, text="Sexo:").grid(row=7, column=0, sticky='e')
tk.Entry(root, textvariable=sexo_var).grid(row=7, column=1)
tk.Label(root, text="Idade:").grid(row=8, column=0, sticky='e')
tk.Entry(root, textvariable=idade_var).grid(row=8, column=1)
tk.Label(root, text="Estado Civil:").grid(row=9, column=0, sticky='e')
tk.Entry(root, textvariable=estado_civil_var).grid(row=9, column=1)
tk.Label(root, text="Profissão:").grid(row=10, column=0, sticky='e')
tk.Entry(root, textvariable=profissao_var).grid(row=10, column=1)
tk.Label(root, text="Cidade:").grid(row=11, column=0, sticky='e')
tk.Entry(root, textvariable=cidade_var).grid(row=11, column=1)
tk.Label(root, text="UF:").grid(row=12, column=0, sticky='e')
tk.Entry(root, textvariable=uf_var).grid(row=12, column=1)
tk.Label(root, text="Endereço:").grid(row=13, column=0, sticky='e')
tk.Entry(root, textvariable=endereco_var).grid(row=13, column=1)
tk.Label(root, text="Turista:").grid(row=14, column=0, sticky='e')
tk.Entry(root, textvariable=turista_var).grid(row=14, column=1)
tk.Label(root, text="Observação:").grid(row=15, column=0, sticky='e')
tk.Entry(root, textvariable=observacao_var).grid(row=15, column=1)

# Botão para Adicionar Ocorrência
tk.Button(root, text="Adicionar", command=add_ocorrencia).grid(row=16, columnspan=2, pady=10)

root.mainloop()
