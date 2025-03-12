# server.py

from flask import Flask
from api import api_blueprint  # Importing API routes
from flask_cors import CORS  # To handle Cross-Origin Resource Sharing (CORS)

app = Flask(__name__)

# Enable CORS if needed (e.g., for frontend-backend communication)
CORS(app)

# Register API routes
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to Cerion's Backend!"

if __name__ == '__main__':
    app.run(debug=True)
