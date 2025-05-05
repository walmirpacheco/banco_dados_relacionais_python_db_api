import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Seiya", "seiya@hot.mail.com.br"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)", (2, "Shiryu", "shiryu@gmail.com"))
    cursor.execute("DELETE FROM clientes WHERE id = 6;")
    conexao.commit()
except Exception as exc:
    print(f"[ERROR!] Ocorreu um erro! {exc}")
    conexao.rollback()