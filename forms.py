import imp
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()]) # 빈칸 시 Data Require
    submit = SubmitField('Submit')
    
    # 5. Refactoring and Forms ; 07:41
    
    
class DeleteTaskFrom(FlaskForm):
    submit = SubmitField('Delete')