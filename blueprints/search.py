from flask import request, jsonify, json, Blueprint

search = Blueprint("search", __name__)


@search.route("/search/<string:searched>", methods=["GET"])
def search_deals(searched):
    return jsonify(searched), 200
