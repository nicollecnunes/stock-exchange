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

#conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/')
def Index():
    # TODO: tirar mock e comentarios - adicionar a consulta em s - adicionar mais row[x] no index.html
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # s = "SELECT * from usuarios"
    # cur.execute(s) # Execute the SQL
    # list_users = cur.fetchall()
    list_users = [{'fname': 'nicolle', 'lname': 'nunes', 'email': 'n@n.com'},
                  {'fname': 'nicolle', 'lname': 'nunes', 'email': 'n@n.com'}]
    return render_template('index.html', list_users=list_users)


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_user(id):
    #TODO: tirar comentarios quando o banco tiver ok
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
    # conn.commit()
    flash('usuario deletado com sucesso')
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
# </string:id></id></id>
