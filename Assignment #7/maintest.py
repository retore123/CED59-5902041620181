#นายจิลลาภัทร คงเรือง 5902041620181 CED 4RA#
#cp -R assignment6 assignment7 คำสั่ง copy ใน GITHUB
#git pull ดึงไฟล์จาก GITHUB
from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class RegisterForm(FlaskForm):
    name = StringField("name", validators=[InputRequired()])
    last = StringField("last", validators=[InputRequired()])
    email = StringField("Email",  [InputRequired("Please enter your email address."), Email("Please enter your email again.")])
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8,max=12, message="Please enter your password 8-12 characters.")])

@app.route('/')
def member():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return "SUBMIT IT OK"
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
