# api.py

from flask import Blueprint, jsonify, request
from database import add_trade, get_db_connection

# Create an API Blueprint for organizing routes
api_blueprint = Blueprint('api', __name__)

# Route to get all trades from the database
@api_blueprint.route('/trades', methods=['GET'])
def get_trades():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trades')
    trades = cursor.fetchall()
    conn.close()

    return jsonify([dict(trade) for trade in trades])  # Convert each row to a dictionary and return as JSON

# Route to add a new trade
@api_blueprint.route('/trades', methods=['POST'])
def post_trade():
    data = request.get_json()
    
    # Ensure required fields are provided
    if not data or not data.get('coin_name') or not data.get('amount') or not data.get('price'):
        return jsonify({'error': 'Missing required fields'}), 400

    coin_name = data['coin_name']
    amount = data['amount']
    price = data['price']

    add_trade(coin_name, amount, price)
    
    return jsonify({'message': 'Trade added successfully'}), 201
