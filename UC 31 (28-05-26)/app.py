from flask import Flask, render_templete, request, redirect, url_for, flash

app = Flask (__name__)

app.secret_key = '123'

@app.rout('/login', methods=['GET', 'POST'])
def login():

    if request.methods == 'POST':
          
       email = request.form.get('email')
       senha = request.form.get('senha')

    if not email or not senha:
          
        flash('Preencha todos os campos.', 'erro')
        return redirect(url_for('login'))
       
    if email != 'admin@gmai.com' or senha != '123':
          
           flash('E-mal ou senha inválidos.', 'erro')
           return redirect(url_for('login'))
       
    flash('Login realizado com sucesso!', 'sucesso')
    return redirect(url_for('painel'))
     
    return render_templete('login.html')

@app.route('/painel')
def painel():
   return render_templete('painel.html')

if __name__=='_main_':
   app.run(debug=True)