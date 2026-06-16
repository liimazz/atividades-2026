from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'minha_chave_secreta_123'

USUARIO = "mago"
SENHA = "4002"


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario == USUARIO and senha == SENHA:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            erro = "Usuário ou senha inválidos!"

    return render_template('login.html', erro=erro)


@app.route('/rotalogin')
def rotalogin():
    return "Esta é a rota extra: rotalogin"


@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        usuario=session['usuario']
    )


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)