from flask import Flask
from flasgger import Swagger

from api.route.alphabet import alphabet_blueprint

app = Flask(__name__)
app.register_blueprint(alphabet_blueprint)
app.config['SWAGGER'] = {
    "title": "Alphabet"
}

swagger = Swagger(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
