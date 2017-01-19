import datetime
from flask import render_template, request, current_app, redirect, flash, url_for
from . import main
from .. import db
from .forms import PersonUpdateForm
from ..models import Person


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Person.query.order_by(Person.modifiedDate.desc()).paginate(page, per_page=current_app.config['PER_PAGE'], error_out=False)
    persons = pagination.items
    return render_template("persons_list.html", persons=persons, pagination=pagination)


@main.route('/person_update/<int:id>', methods=['GET', 'POST'])
def person_update(id):
    person = Person.query.get_or_404(id)
    form = PersonUpdateForm(person=person)
    if form.validate_on_submit():
        person.name = form.name.data
        person.gender = int(form.gender.data)
        person.birthday = form.birthday.data
        person.age = int(form.age.data)
        person.location = form.location.data
        person.comment = form.comment.data
        db.session.add(person)
        db.session.commit()
        flash('资料已更新')
        return redirect(url_for('.index'))
    form.name.data = person.name
    form.gender.data = person.gender
    form.birthday.data = person.birthday
    form.age.data = person.age
    form.location.data = person.location
    form.comment.data = person.comment
    return render_template('edit_person.html', form=form)
