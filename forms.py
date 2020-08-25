from flask_wtf import FlaskForm, CsrfProtect
from wtforms import TextField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email

csrf = CsrfProtect()

class ContactForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired(message="Please enter your name.")], render_kw={"placeholder": "Name"})
    email = TextField("Email Address", validators=[DataRequired(message="Please enter your email address."),Email()], render_kw={"placeholder": "Email Address"})
    phone = TextField('Phone Number', validators=[DataRequired(message="Please enter your phone number.")], render_kw={"placeholder": "Phone Number"})    
    message = TextAreaField("Message", validators=[DataRequired(message="Please enter a message.")], render_kw={"placeholder": "Message"})
    submit = SubmitField("Send")
