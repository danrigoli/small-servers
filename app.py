from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Lista de frases
frases = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "La paciencia es un árbol de raíz amarga, pero de frutos muy dulces.",
    "No hay viento favorable para el que no sabe a dónde va.",
    "La vida es lo que hacemos de ella.",
    "El conocimiento es poder."
]

# Endpoint para devolver una frase al azar
@app.route('/frase', methods=['GET'])
def obtener_frase():
    frase = random.choice(frases)
    return jsonify({'frase': frase})

# Endpoint para sumar dos parámetros
@app.route('/sumar', methods=['GET'])
def sumar():
    # Obtener los parámetros 'a' y 'b' de la solicitud
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    suma = a + b
    return jsonify({'suma': suma})

if __name__ == '__main__':
    app.run(debug=True)
