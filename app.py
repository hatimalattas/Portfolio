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
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail()

mail.init_app(app)

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
          msg = Message('Message from my portfolio website', sender='7atem96@gmail.com', recipients=['alattas96@outlook.com'])
          msg.body = """
          From: %s %s <%s>
          %s
          """ % (form.name.data, form.phone.data, form.email.data, form.message.data)
          mail.send(msg)
          flash('Thank you for contacting me, your message has been successfully sent to my mailbox.', 'success')
          return render_template('index.html', form=form)

    elif request.method == 'GET':
        return render_template('index.html', form=form)

@app.route('/download')
def download_file():
  path = "HatimAlattasResume-SE.pdf"
  return send_file(path,as_attachment=True)

if __name__ == '__main__':
    app.run()
    
