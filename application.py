from flask import Flask

from blueprints.search import search

app = Flask(__name__, static_url_path="")

app.register_blueprint(search, url_prefix="/api")


@app.route("/")
def index_page():
    return app.send_static_file("index.html")
