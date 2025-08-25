from flask import Blueprint

# Criação do Blueprint chamado "main"
main = Blueprint('main', __name__)

# Importa as rotas associadas ao blueprint
from . import routes
