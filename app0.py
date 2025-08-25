import os
from app import create_app

# Pega o ambiente de configuração de variável FLASK_CONFIG
config_name = os.getenv('FLASK_CONFIG') or os.getenv('FLASK_ENV') or 'default'

# Cria a aplicação Flask com base na configuração
app = create_app(config_name)

print(f"[DEBUG] app.debug = {app.debug}")
print(f"[DEBUG] config_name = {config_name}")

if __name__ == '__main__':
    app.run()
