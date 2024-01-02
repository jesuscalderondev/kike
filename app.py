from flask import Flask, render_template, redirect, Blueprint, jsonify, request
from flask import session as cookies
from dotenv import load_dotenv
from os import getenv
#locals imports
from database import *
from functions import *



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#equipments

equipements = Blueprint('equipments', __name__, url_prefix='/equipments')

@equipements.route('/create', methods=['GET', 'POST'])
@requiredSession
def createEquipment():
    if request.method == 'GET':
        return render_template('/equipments/create.html')
    elif request.method == 'POST':
        data = request.get_json()
        return "SIu"


if __name__ == "__main__":
    load_dotenv()
    Base.metadata.create_all(engine)
    app.run(debug=True)