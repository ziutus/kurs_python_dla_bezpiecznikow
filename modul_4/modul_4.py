from flask import Flask, request, render_template
from flask.templating import render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


db.create_all()


@app.route("/", methods=["GET"])
def hello():
    hello = request.args.get('hello')
    hello2 = request.args.get('hello2')
    template = '''<!DOCTYPE html>
    <html>
    <head>
    <title>Login</title>
    </head>
    <body>

    <h1>{{hello}}</h1>
    <p>''' + hello2 + '''</p>

    </body>
    </html>'''
    return render_template_string(template, hello=hello)


@app.route('/login', methods=["GET"])
def login_page():
    return render_template('login.html')


@app.route("/login", methods=["POST"])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    user = User.query.filter_by(login=login, password=password).first()
    # if user:
    #     return render_template(
    #         'post_login.html',
    #         header='Success!',
    #         message=f'Logged in as {user.login}'
    #         )
    # return render_template(
    #     'post_login.html',
    #     header='Login failed.',
    #     message='Invalid credentials'
    #     )

    return render_template('post_login2.html', user=user)


@app.route('/register', methods=["GET"])
def register_page():
    return render_template('register.html')


@app.route("/register", methods=["POST"])
def register():
    login = request.form.get('login')
    password = request.form.get('password')

    user = User(login=login, password=password)
    db.session.add(user)
    db.session.commit()

    return render_template('welcome.html', name=login)


if __name__ == "__main__":
    app.run('127.0.0.1', '8888')