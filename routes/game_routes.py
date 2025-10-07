from flask import Blueprint, request  
from controllers.game_controllers import get_games, create_game, get_game_by_id 

# Define um Blueprint para as rotas de "Game"
game_routes = Blueprint('game_routes', __name__)  

# Rota para listar todos os games (GET)
@game_routes.route('/Game', methods=['GET'])
def games_get():
    return get_games()

# Rota para buscar um game pelo ID (GET)
@game_routes.route('/Game/<int:game_id>', methods=['GET'])
def game_get_by_id(game_id):
    return get_game_by_id(game_id)

# Rota para criar um novo game (POST)
@game_routes.route('/Game', methods=['POST'])
def games_post():
    return create_game(request.json)
