from flask import render_template, jsonify
from . import main
from ..models import Person


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('persons_list.html')


@main.route('/load_datalist', methods=['POST'])
def load_datalist():
    return jsonify(title=666)
