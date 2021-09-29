from flask import Flask

from ingredients.api import api

flask_app = Flask('ingredients_app')
flask_app.register_blueprint(api)

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000)
