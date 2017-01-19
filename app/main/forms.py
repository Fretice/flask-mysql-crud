from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import Required, NumberRange


class PersonUpdateForm(Form):
    name = StringField('姓名', validators=[Required()])
    gender = SelectField('性别', choices=[('1', '男'), ('0', '女')])
    birthday = DateField('生日')
    age = IntegerField('年龄')
    location = StringField('地点')
    comment = StringField('备注')
    submit = SubmitField('保存')
