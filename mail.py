from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '168108385@qq.com'
app.config['MAIL_PASSWORD'] = 'oomjybvnncblbgfc'

mail = Mail(app)

msg = Message('test',sender="168108385@qq.com",recipients=["chenkaiyue2008@163.com"])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
	mail.send(msg)
