import sqlite3

def criar_banco():
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

def adicionar_contato(nome, telefone, email):
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)', (nome, telefone, email))

    conexao.commit()
    conexao.close()

def listar_contatos():
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()

    conexao.close()
    return contatos

def atualizar_contato(id, nome, telefone, email):
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('UPDATE contatos SET nome=?, telefone=?, email=? WHERE id=?', (nome, telefone, email, id))
    conexao.commit()
    conexao.close()

def deletar_contato(id):
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM contatos WHERE id=?', (id,))
    conexao.commit()
    conexao.close()
