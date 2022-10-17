# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2  # pip install psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "bcc321-bd"

DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "admin"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

with open('init.sql', 'r') as file:
    initSQL = file.read()

    cur.execute(initSQL)
    conn.commit()

cur.execute('select * from usuario')
recset = cur.fetchall()
for rec in recset:
    print(rec)

@app.route('/')
def Index():
    list_users = [[123, 'Nicolle', 'nicollecnunes', 'Diamantina'], [234, 'Nicolle',
                                                                    'nicollecnunes', 'Diamantina'], [543, 'Nicolle', 'nicollecnunes', 'Diamantina']]
    return render_template('index.html', list_users=list_users, list_ativos=[])


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_user(id):
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
    # conn.commit()
    return redirect(url_for('Index'))

@app.route('/consultar-ativos/<string:id>', methods=['POST', 'GET'])
def consultar_ativos(id):
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # s = 'SELECT CodigoAtivo, Tipo FROM FundoInvestimentos WHERE CodigoUsuario = {0}'.format(id)
    # s2 = 'SELECT Nome FROM Usuarios WHERE CodigoUsuario = {0}'.format(id)

    # cur.execute(s)
    # list_ativos = cur.fetchall()

    # cur.execute(s2)
    # nome_user = cur.fetch() 

    nome_user = "Nicolle"
    list_ativos = [[1, 'Tipo B'], [3, 'Tipotipo']]
    return render_template('index.html', list_ativos=list_ativos, nome_user=nome_user)


@app.route('/consulta-por-data/<de>/<ate>')
def consulta_por_data(de=None, ate=None):
     # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # s = 'SELECT ...'

    # cur.execute(s)
    # list_investimentos = cur.fetchall()

    list_investimentos = [[550, 23, '02-02-2022'], [550, 23, '02-02-2022']]
    return render_template('index.html', list_investimentos=list_investimentos, dataDe=de, dataAte=ate)

@app.route('/investimentos-por-analistas')
def investimentos_analistas():
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # s = 'SELECT ...'

    # cur.execute(s)
    # list_investimentos_analistas = cur.fetchall()

    list_investimentos_analistas = [['nome analista 1', 53350, 2, '02-02-2022' ], ['nome analista 2', 50, 23, '02-02-2022']]
    return render_template('index.html', list_investimentos_analistas=list_investimentos_analistas)

if __name__ == "__main__":
    app.run(debug=True)
# </string:id></id></id>
