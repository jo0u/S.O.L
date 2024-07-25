import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('registro_ocorrencia.db')
cursor = conn.cursor()

# Criar a tabela 'topicos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS topicos (
    id INTEGER PRIMARY KEY,
    tipo TEXT  NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Criar a tabela 'ocorrencias'
cursor.execute('''
CREATE TABLE IF NOT EXISTS ocorrencias (
    id INTEGER PRIMARY KEY,
    data DATE  NULL,
    hora TIME  NULL,
    posto TEXT  NULL,
    topicos_id INTEGER  NULL,
    nome_salva_vidas TEXT  NULL,
    nome_vitima TEXT  NULL,
    grau TEXT  NULL,
    sexo INTEGER  NULL,
    idade INTEGER  NULL,
    estado_civil TEXT  NULL,
    profissao TEXT  NULL,
    cidade TEXT  NULL,
    uf TEXT  NULL,
    endereco TEXT  NULL,
    turista BOOLEAN  NULL,
    observacao TEXT  NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (topicos_id) REFERENCES topicos(id)
)
''')

# Inserir alguns dados de exemplo
cursor.execute("INSERT INTO topicos (tipo) VALUES ('Afogamento')")
cursor.execute("INSERT INTO topicos (tipo) VALUES ('Prevenção')")
cursor.execute("INSERT INTO topicos (tipo) VALUES ('Obito')")
cursor.execute('''
INSERT INTO ocorrencias (data, hora, posto, topicos_id, nome_salva_vidas, nome_vitima, grau, sexo, idade, estado_civil, profissao, cidade, uf, endereco, turista, observacao)
VALUES ('2024-07-25', '14:30', 'Posto 1', 1, 'Salva Vidas 1', 'Vítima 1', 'Grave', 1, 30, 'solteiro', 'Professor', 'Cidade A', 'UF', 'Rua A', 1, 'Nenhuma')
''')

# Salvar e fechar a conexão
conn.commit()
conn.close()
