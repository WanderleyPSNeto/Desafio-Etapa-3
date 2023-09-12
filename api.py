# Importa as bibliotecas necessárias
from flask import Flask, request, jsonify

# Cria uma instância do Flask
app = Flask(__name__)

# Lista para armazenar os personagens
personagens = []

# Função para criar um novo personagem
def criar_personagem():

    # Obtém as informações do personagem do request
    nome = request.json['nome']
    descricao = request.json['descricao']
    link_imagem = request.json['link_imagem']
    programa = request.json['programa']
    animador = request.json['animador']

    # Cria um novo personagem com as informações obtidas
    personagem = {
        'nome': nome,
        'descricao': descricao,
        'link_imagem': link_imagem,
        'programa': programa,
        'animador': animador
    }

    # Adiciona o novo personagem à lista de personagens
    personagens.append(personagem)

    # Retorna uma resposta com o status 201 (Created)
    return jsonify({'status': 201})

# Função para recuperar todos os personagens
def recuperar_personagens():

    # Retorna uma lista de personagens
    return jsonify({'personagens': personagens})

# Define o endpoint para criar um novo personagem
@app.route('/characters/', methods=['POST'])
def criar_personagem_endpoint():

    # Chama a função para criar um novo personagem
    return criar_personagem()

# Define o endpoint para recuperar todos os personagens
@app.route('/characters/', methods=['GET'])
def recuperar_personagens_endpoint():

    # Chama a função para recuperar todos os personagens
    return recuperar_personagens()

# Inicia o servidor Flask
app.run(debug=True)
