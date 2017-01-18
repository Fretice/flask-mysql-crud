from flask import render_template, jsonify, request, current_app
from . import main
from ..models import Person


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Person.query.order_by(Person.modifiedDate.desc()).paginate(page, per_page=current_app.config['PER_PAGE'], error_out=False)
    persons = pagination.items
    return render_template("persons_list.html", persons=persons, pagination=pagination)
