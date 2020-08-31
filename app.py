import os
from flask import Flask, render_template, request, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import ContactForm
from flask_mail import Mail, Message
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


##########################
#### APP CONFIG. ######
##########################
app = Flask(__name__)
app.config.from_object('config')

# set configuration and instantiate mail
# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": os.environ['EMAIL_USER'],
#     "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
# }

# print(os.environ['EMAIL_USER'])
# print(os.environ['EMAIL_USER'])

# app.config.update(mail_settings)
# mail = Mail(app)

# mail_settings = {
#     "MAIL_SERVER": 'smtp.sendgrid.net',
#     "MAIL_PORT": 465,
#     "MAIL_USERNAME": os.environ['EMAIL_USER'],
#     "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD'],
#     "USERNAME": 'apikey',
#     "PASSWORD": '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'
# }

# app.config.update(mail_settings)
# mail = Mail(app)

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

# mail = Mail()
# app.config["MAIL_SERVER"] = "smtp-mail.outlook.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = 'alattas96@outlook.com'
# app.config["MAIL_PASSWORD"] = '1996Ha()'

# mail.init_app(app)

# app.config.update(dict(
#     DEBUG = True,
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = 587,
#     MAIL_USE_TLS = True,
#     MAIL_USE_SSL = False,
#     MAIL_USERNAME = '7atem96@gmail.com',
#     MAIL_PASSWORD = '(1996)Ha',
# ))

# mail = Mail(app)

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
                        recipients=["alattas96@outlook.com"], # replace with your email for testing
                        body="This is a test email I sent with Gmail and Python!")

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
    


        # else:
        #   msg = Message('Message from my portfolio website', sender='alattas96@outlook.com', recipients=['7atem96@gmail.com'])
        #   msg.body = """
        #   From: %s %s <%s>
        #   %s
        #   """ % (form.name.data, form.phone.data, form.email.data, form.message.data)
        #   mail.send(msg)

            #         msg = Message(subject="Hello",
            #             sender=app.config.get("MAIL_USERNAME"),
            #             recipients=["alattas96@outlook.com"], # replace with your email for testing
            #             body="This is a test email I sent with Gmail and Python!")

            # mail.send(msg)