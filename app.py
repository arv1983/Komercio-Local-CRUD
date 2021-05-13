from flask import Flask, request, jsonify
from db.db import products





app = Flask(__name__)

@app.route('/products/')
def list_products():
    return jsonify(products)


@app.route('/products/<product_id>')
def get(product_id: int):
    for product in products:
        if product['id'] == int(product_id):
            return jsonify(product)
    return ('', 404)


@app.route('/products', methods=['POST'])
def create():
    product_data = request.json
    if product_data.get('name') and product_data.get('price'):
        id = max(products, key=lambda p: p['id'])['id'] + 1
        product_created = {"id": id,
            "name": product_data.get('name'),
            "price": product_data.get('price')}
        return jsonify(product_created)
    return ('', 404)


@app.route('/products/<product_id>', methods=['PATCH'])
def update(product_id: int):
    product_data = request.json
    if product_id:
        for product in products:
            if product['id'] == int(product_id):
                if product_data.get('name'):
                    product['name'] = product_data.get('name')
                if product_data.get('price'):
                    product['price'] = product_data.get('price')
                return ''

    return ('', 404)


@app.route('/products/<product_id>', methods=['DELETE'])
def delete(product_id: int):
    product_data = request.json
    if product_id:
        for product in products:
            if product['id'] == int(product_id):
                products.remove(product)
                return jsonify(products)
    return ('', 404)