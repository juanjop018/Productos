
#trabajo restapi
#Juan Jose Peña Quiñonez
#Ficha:2502640
from flask import Flask, jsonify, request

app = Flask(__name__)

from productos import productos


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


@app.route('/productos')
def getProductos():
   
    return jsonify({'productos': productos})


@app.route('/productos/<string:productos_name>')
def getProductos(productos_name):
    productosFound = [
        productos for productos in productos if productos['name'] == productos_name.lower()]
    if (len(productosFound) > 0):
        return jsonify({'productos': productosFound[0]})
    return jsonify({'message': 'Productos Not found'})


@app.route('/productos', methods=['POST'])
def addProductos():
    new_productos = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    productos.append(new_productos)
    return jsonify({'productos': productos})


@app.route('/productos/<string:productos_name>', methods=['PUT'])
def editProductos(productos_name):
    productosFound = [productos for productos in productos if productos['name'] == productos_name]
    if (len(productosFound) > 0):
        productosFound[0]['name'] = request.json['name']
        productosFound[0]['price'] = request.json['price']
        productosFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Productos Updated',
            'productos': productosFound[0]
        })
    return jsonify({'message': 'Productos Not found'})


@app.route('/productos/<string:productos_name>', methods=['DELETE'])
def deleteProductos(productos_name):
    productosFound = [productos for productos in productos if productos['name'] == productos_name]
    if len(productosFound) > 0:
        productos.remove(productosFound[0])
        return jsonify({
            'message': 'Productos Deleted',
            'products': productos
        })

if __name__ == '__main__':
    app.run(debug=True, port=3000)
