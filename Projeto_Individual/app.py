from flask import Flask,render_template,request,redirect

class cadPersonagem:
    def __init__(self,idOnePiece,nome,tripulacao,recompensa,frutadoDiabo):
        self.idOnePiece = idOnePiece
        self.nome = nome
        self.tripulacao = tripulacao
        self.recompensa = recompensa
        self.frutadoDiabo = frutadoDiabo

listaPersonagem = []

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Personagem one piece'

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de One Piece')

@app.route('/criar', methods=['POST'])
def criar():
    idOnePiece = request.form['ID-onePiece']
    nome = request.form['Nome']
    tripulacao = request.form['Tripulacao']
    recompensa = request.form['Recompensa']
    frutadoDiabo = request.form['FrutadoDiabo']
    obj = cadPersonagem(idOnePiece, nome, tripulacao, recompensa, frutadoDiabo)
    listaPersonagem.append(obj)
    return redirect('/personagens')

@app.route('/personagens')
def personagens():
    return render_template('Personagens.html', Titulo='Personagens', listaPersonagem=listaPersonagem)

@app.route('/excluir/<idOnePiece>', methods = ['GET', 'DELETE'])
def excluir(idOnePiece):
    for i, pers in enumerate(listaPersonagem):
        if pers.idOnePiece == idOnePiece:
            listaPersonagem.pop(i)
            break
    return redirect('/personagens')

@app.route('/editar/<idOnePiece>', methods = ['GET'])
def editar(idOnePiece):
    for i, pers in enumerate(listaPersonagem):
        if pers.idOnePiece == idOnePiece:
            return render_template('editar.html', Titulo='Editar Personagem',Personagem=pers)

@app.route('/alterar', methods = ['POST', 'PUT'])
def alterar():
    id = request.form['ID-onePiece']
    for i, pers in enumerate(listaPersonagem):
        if pers.idOnePiece == id:
            pers.nome = request.form['Nome']
            pers.tripulacao = request.form['Tripulacao']
            pers.recompensa = request.form['Recompensa']
            pers.frutadoDiabo = request.form['FrutadoDiabo']

        return redirect('/personagens')
if __name__ == '__main__':
    app.run()