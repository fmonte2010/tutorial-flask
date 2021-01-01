from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import (StringField, SubmitField, TextAreaField, BooleanField)

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título Slug', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')

class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')
