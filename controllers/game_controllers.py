from models.game_models import Game  # Importa o modelo Game
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os games
def get_games():
    games = Game.query.all()  # Busca todos os games no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de games.',
            'dados': [game.json() for game in games]  # Converte os objetos de game para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para obter um game específico por ID
def get_game_by_id(game_id):
    game = Game.query.get(game_id)  # Busca o game pelo ID
    
    if game:  # Verifica se o game foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'Game encontrado.',
                'dados': game.json()  # Converte os dados do game para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o game não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'Game não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo game
def create_game(game_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in game_data for key in ['titulo', 'genero', 'desenvolvedor', 'plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvedor e plataforma são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo game
    novo_game = Game(
        titulo=game_data['titulo'],
        genero=game_data['genero'],
        desenvolvedor=game_data['desenvolvedor'],
        plataforma=game_data['plataforma']
    )
    
    db.session.add(novo_game)  # Adiciona o novo game ao banco de dados
    db.session.commit()  # Confirma a transação no banco
    
    # Resposta de sucesso com os dados do novo game
    response = make_response(
        json.dumps({
            'mensagem': 'Game cadastrado com sucesso.',
            'game': novo_game.json()  # Retorna os dados do game cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response
