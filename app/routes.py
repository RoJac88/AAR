from app import app, get_db
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def home():
    db = get_db()
    c = db.cursor()
    if request.method == 'GET':
        c.execute('SELECT * FROM produtos')
        prods = c.fetchall()
        return render_template('home.html', prods=prods)
    if request.method == 'POST':
        print(request.form)
        name = request.form.get('nome') or None
        q = request.form.get('qtd') or None 
        price = request.form.get('preco') or None 
        if name and q and price:
            prod = (name, q, price)
            c.execute("INSERT INTO produtos VALUES (?,?,?)", prod)
            db.commit()
            print('Produto inserido')
        return redirect(url_for('home'))
        # O redirecionamento evita que o formulário seja reenviado ao atualizar a página
