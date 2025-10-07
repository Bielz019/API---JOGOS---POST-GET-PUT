# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

# Define a classe Game que representa a tabela 'games' no banco de dados
class Game(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'games'  

    # Define as colunas da tabela 'games'
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID do game, chave primária
    titulo = db.Column(db.String(80), nullable=False)  # Coluna para o modelo do game, não pode ser nulo
    genero = db.Column(db.String(80), nullable=False)  # Coluna para a marca do game, não pode ser nulo
    desenvolvedor = db.Column(db.String(80), nullable=False)  # Coluna para o ano do game, não pode ser nulo
    plataforma = db.Column(db.String(80), nullable=False)
    

    # Método para retornar os dados do game como um dicionário
    def json(self):  
        return {
            'id': self.id,  # ID do game
            'titulo': self.titulo,  
            'genero': self.genero,  
            'desenvolvedor': self.desenvolvedor,
            'plataforma': self.plataforma
        }
