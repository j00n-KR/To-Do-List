import imp
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm():
    title = StringField('Title', validators=[])
    submit = SubmitField('Submit')
    
    # 5. Refactoring and Forms ; 07:41