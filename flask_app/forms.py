from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, validators, ValidationError

roll_list = ['rk', 'naren', 'yogesh', 'karan', '154076022','15D070032','15D070051', '15D070033' ,'160070049','160100059','16D070023','16D070024','16D070026','16D070030','16D070049','16D070059','16D070062','170070002','170070016','170070041','173074002','173074016','173074017','17D070020','17D070022','17D070039','17D070051','17D070054','17D070058','17D070060','17D070061','17D070063','183074002','183074009','183074017','183074018','183074022','183170012','183170021','184073001','184073004','18I170013','193070024','193070076','193076001','194076011','194366003','16D070027','16D070029']

def roll_check(form, field):
    if field.data not in roll_list:
        raise ValidationError('Enter the Roll number enrolled in EE765')

class InputForm(FlaskForm):
    """Form to take roll number and Data Points"""
    rollno = StringField('Roll number', [validators.Required("Please enter your roll number."), roll_check])
    points = IntegerField('Data Points (10-1000)', [validators.Required("Please enter a number between 10 and 1000"), validators.NumberRange(min=10, max=1000)])
    submit = SubmitField('Download')
