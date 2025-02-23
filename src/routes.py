from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"mensaje": "Backend funcionando correctamente"})

# Verifying fetch conection

@main.route('/dashboard/objectives', methods=['POST'])
def get_data():
    data = request.get_json()
    print("Datos recibidos:", data)
    return jsonify({"message": "Datos recibidos"}), 200
