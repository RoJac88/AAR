from flask import Flask, g
import sqlite3

DATABASE = 'example.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produtos';")
        tables = c.fetchall()
        if len(tables) == 0:
            c.execute("CREATE TABLE produtos (nome text, qtd integer, price real)")
            print("Tabela criada")
            conn.commit()
        else: 
            print("Tabela encontrada")

init_db()

from app import routes 
