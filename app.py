from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class cadinfluencer:
    def __init__(self, nome, plataformasSociais, numeroSeguidores, areaInteresse):
        self.nome = nome
        self.plataformasSociais = plataformasSociais
        self.numeroSeguidores = numeroSeguidores
        self.areaInteresse = areaInteresse


Lista = []


@app.route('/influencer')
def influencer():
    return render_template('Influencers.html', Titulo = 'Influencer Cadastrados: ', ListaInfluencers = Lista)


@app.route('/')
def inicio():
    return 'Começando'


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = 'Cadastro de Influenciadores')


@app.route("/criar", methods = ['POST'])
def criar():
    nome = request.form['nome']
    plataformasSociais = request.form['plataformasSociais']
    numeroSeguidores = request.form['numeroSeguidores']
    areaInteresse = request.form['areaInteresse']

    obj = cadinfluencer(nome, plataformasSociais, numeroSeguidores, areaInteresse)

    Lista.append(obj)

    return redirect('/influencer')


if __name__ == '__main__':
    app.run()
