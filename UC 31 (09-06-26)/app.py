from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicio():

    nome = request.cookies.get('nome')
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        'inicio.html',
        nome=nome,
        tema=tema
    )


@app.route('/salvar_nome', methods=['POST'])
def salvar_nome():

    nome = request.form.get('nome')

    response = make_response(redirect(url_for('inicio')))

    response.set_cookie('nome', nome, max_age=60 * 60 * 24 * 30)

    return response


@app.route('/tema/<escolha>')
def trocar_tema(escolha):

    if escolha not in ['claro', 'escuro']:
        return redirect(url_for('inicio'))

    response = make_response(redirect(url_for('inicio')))

    response.set_cookie('tema', escolha, max_age=60 * 60 * 24 * 30)

    return response


if __name__ == '__main__':
    app.run(debug=True)