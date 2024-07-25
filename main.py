import os
import subprocess
import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, W, E
from tkinter.messagebox import showinfo
from datetime import datetime

# Função para buscar ocorrências com base nas datas de início e fim
def fetch_ocorrencias(start_date, end_date):
    conn = sqlite3.connect('registro_ocorrencia.db')
    cursor = conn.cursor()
    query = '''
    SELECT
        (SELECT COUNT(*) FROM ocorrencias WHERE data BETWEEN ? AND ? AND grau = 'Óbito') AS obitos,
        (SELECT COUNT(*) FROM ocorrencias WHERE data BETWEEN ? AND ? AND grau = 'Prevenção') AS prevencoes,
        (SELECT COUNT(*) FROM ocorrencias WHERE data BETWEEN ? AND ? AND grau = 'Salvamento Não Fatal') AS salvamentosNF,
        (SELECT COUNT(*) FROM ocorrencias WHERE data BETWEEN ? AND ? AND grau = 'Criança Encontrada') AS criancasEncontradas,
        (SELECT COUNT(*) FROM ocorrencias WHERE data BETWEEN ? AND ? AND grau = 'S.O.S') AS sos
    '''
    cursor.execute(query, (start_date, end_date, start_date, end_date, start_date, end_date, start_date, end_date, start_date, end_date))
    results = cursor.fetchone()
    conn.close()
    return results

# Função para atualizar os dados exibidos na interface
def update_stats():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    if not start_date or not end_date:
        showinfo("Erro", "Por favor, preencha ambas as datas.")
        return

    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        showinfo("Erro", "Formato de data inválido. Use AAAA-MM-DD.")
        return

    stats = fetch_ocorrencias(start_date, end_date)
    obitos_var.set(stats[0])
    prevencoes_var.set(stats[1])
    salvamentosNF_var.set(stats[2])
    criancasEncontradas_var.set(stats[3])
    sos_var.set(stats[4])

# Função para abrir o script add_ocorrencia.py
def open_add_ocorrencia():
    subprocess.run(['python', 'add_ocorrencia.py'])

# Configuração da janela principal
root = Tk()
root.title("Sistema de Ocorrências")

# Variáveis
start_date_var = StringVar()
end_date_var = StringVar()
obitos_var = StringVar()
prevencoes_var = StringVar()
salvamentosNF_var = StringVar()
criancasEncontradas_var = StringVar()
sos_var = StringVar()

# Frame para os filtros de data
filter_frame = Frame(root)
filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)

Label(filter_frame, text="Data de Início:").grid(row=0, column=0, sticky=W)
Entry(filter_frame, textvariable=start_date_var).grid(row=0, column=1)

Label(filter_frame, text="Data de Fim:").grid(row=1, column=0, sticky=W)
Entry(filter_frame, textvariable=end_date_var).grid(row=1, column=1)

Button(filter_frame, text="Filtrar", command=update_stats).grid(row=2, columnspan=2, pady=10)

# Frame para exibir as estatísticas
stats_frame = Frame(root)
stats_frame.grid(row=1, column=0, padx=10, pady=10)

Label(stats_frame, text="Óbitos:").grid(row=0, column=0, sticky=W)
Label(stats_frame, textvariable=obitos_var).grid(row=0, column=1, sticky=E)

Label(stats_frame, text="Prevenções:").grid(row=1, column=0, sticky=W)
Label(stats_frame, textvariable=prevencoes_var).grid(row=1, column=1, sticky=E)

Label(stats_frame, text="Salvamentos Não Fatais:").grid(row=2, column=0, sticky=W)
Label(stats_frame, textvariable=salvamentosNF_var).grid(row=2, column=1, sticky=E)

Label(stats_frame, text="Crianças Encontradas:").grid(row=3, column=0, sticky=W)
Label(stats_frame, textvariable=criancasEncontradas_var).grid(row=3, column=1, sticky=E)

Label(stats_frame, text="S.O.S Praia & S.O.S Via Pública:").grid(row=4, column=0, sticky=W)
Label(stats_frame, textvariable=sos_var).grid(row=4, column=1, sticky=E)

# Botões de Ações
Button(root, text="Nova Ocorrência", command=open_add_ocorrencia).grid(row=2, column=0, pady=10, sticky=W)
Button(root, text="Ver Dados", command=lambda: showinfo("Ação", "Função para consultar dados")).grid(row=2, column=0, pady=10, sticky=E)

# Executar a aplicação
root.mainloop()
