import random
import string

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

from .models import URLmodel

class URLForm(FlaskForm):
    original_url = StringField('Вставьте ссылку',
                               validators=[DataRequired(message='Ссылка не может быть пустой'),
                                           URL(message='Неверная сслыка')])
    submit = SubmitField('Получить короткую ссылку')


def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=6))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short