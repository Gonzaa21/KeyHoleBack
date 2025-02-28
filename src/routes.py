from flask import Blueprint, request, jsonify
from src.models import db, Transactions

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"mensaje": "Backend funcionando correctamente"})

# Verifying fetch conection (✅)

@main.route('/dashboard/objectives', methods=['POST'])
def get_data():
    data = request.get_json()
    print("Datos recibidos:", data)
    return jsonify({"message": "Datos recibidos"}), 200

# Save data in database (❌)

@main.route('/dashboard/income', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()  # Recibe JSON from front
        
        # Extract data from JSON
        new_transaction = Transactions(
            amount=data['amount'],
            months=data['months'],
            category=data.get('category'),  # Opcional
            trans_type=data['trans_type']
        )

        db.session.add(new_transaction)  # Add to keyhole database
        db.session.commit()  # Save changes

        return jsonify({'message': 'Transaction added successfully!'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
