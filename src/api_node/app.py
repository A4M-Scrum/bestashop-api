from flask import Flask, jsonify, request

from api_node.database import getall_categories
from database import getall_products, bshop_db

app = Flask(__name__)

database = bshop_db()
database.set_conn(user = 'remote',host = '10.3.3.205', database = 'bestashop_db')
@app.route("/")
def home():
    if request.method == "GET":
        try:
            products = getall_products(database)
            return jsonify(products)
        except:
            return "Oops, something went wrong! Please, try again later."
    else: return "Hello world"

@app.route("/categories")
def categories_endpoint():
    if request.method == "GET":
        try:
            products = getall_products(database)
            return jsonify(products)
        except:
            return "Oops, something went wrong! Please, try again later."
    else: return "Hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

print("hello world")