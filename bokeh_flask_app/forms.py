from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators

class InputForm(FlaskForm):

    """Form to take roll number and Data Points"""

    rollno = StringField('Roll number')
    points = IntegerField('Data Points', [validators.NumberRange(min=10, max=1000)])
    submit = SubmitField('Download')
