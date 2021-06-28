import os
from flask import Flask, render_template, request, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import ContactForm
from flask_mail import Mail, Message


##########################
#### APP CONFIG. ######
##########################
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
port = int(os.environ.get("PORT", 5000))

# set configuration and instantiate mail
mail_settings = {
    "MAIL_SERVER": 'smtp.office365.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}
app.config.update(mail_settings)
mail = Mail(app)

##########################
####### ROUTES ###########
##########################
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit() == False:
            return render_template('index.html', form=form)

        else:
            msg = Message(subject="Hello",
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=["alattas96@outlook.com"],
                        body="""
                        From: %s %s <%s>
                        %s
                        """ % (form.name.data, form.phone.data, form.email.data, form.message.data))

            mail.send(msg)
            flash('Thank you for contacting me, your message has been successfully sent to my mailbox.', 'success')
            return render_template('index.html', form=form)

    elif request.method == 'GET':
        return render_template('index.html', form=form)

@app.route('/download')
def download_file():
  path = "./static/assets/HatimAlattasResume-SE.pdf"
  return send_file(path,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)