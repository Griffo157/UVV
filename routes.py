from flask import current_app, jsonify
from . import main

@main.route('/')
@main.route('/index')
def index():
    ambiente = current_app.config.get("CONFIG_NAME", "desconhecido")
    return jsonify(message= "Ola, mundo", ambiente=ambiente)
