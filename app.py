from chalice import Chalice

from chalicelib.api.route.alphabet_api import alphabet_blueprint

app = Chalice(app_name="alphabet")
app.register_blueprint(alphabet_blueprint)
