from flask import request, render_template, Flask, jsonify
from flask_cors import CORS
from database import generate_random_weapon, generate_random_armor

app = Flask(__name__)

CORS(app)

@app.route('/')
def generate_loot():
    weapon = generate_random_weapon()
    armor = generate_random_armor()
    return jsonify({"weapon": weapon, "armor": armor})
