from flask import request, jsonify, json, Blueprint
import requests
import json

search = Blueprint("search", __name__)


@search.route("/search/deals/<string:searched>", methods=["GET"])
def get_deals(searched):
    params = {
        "spider_name": "amazon_spider",
        "start_requests": True,
    }
    response = requests.get("http://localhost:9080/crawl.json", params)
    data = json.loads(response.text)

    sorted_data = sorted(data["items"], key=lambda i: (i["price"]))

    return jsonify(sorted_data), 200

