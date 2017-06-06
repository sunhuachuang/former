from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

class User:
    username = '' # Text
    email = ''    # Email
    password = '' # RepeatedType
    age = 0       # Int
    desc = ''     # Textarea
    website = ''  # Url
    photo   = ''  # File
    birthday = '' # Date

    @staticmethod
    def save(user):
        pass

    @staticmethod
    def find(id):
        pass

class UserForm:
    pass

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/<id>')
def show_user(id):
    user = User.find(id)
    form = UserForm(user)
    if form.is_valid:
        User.save(user)
        pass

    return render_template('show.html')

if __name__ == '__main__':
    app.run()
