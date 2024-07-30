from flask import Flask, render_template, redirect, url_for, flash
import flask_wtf
import wtforms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'

class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Ваше імя', validators=[wtforms.validators.DataRequired()])
    surname = wtforms.StringField('Ваше прізвище', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('продовжити')

@app.route('/', methods=['GET', 'POST'])
def web():
    form = SubscriptionForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        # Process the form data (e.g., save to database)
        flash('Операція пройшла успішно!', 'success')
        return redirect(url_for('web'))  # Redirect to avoid form resubmission
    return render_template("web1.html", form=form)

@app.route('/web2')
def web2():
    return render_template("web2.html")

@app.route('/web3')
def web3():
    return render_template("web3.html")

@app.route('/web4')
def web4():
    return render_template("web4.html")

@app.route('/web5')
def web5():
    return render_template("web5.html")

@app.route('/web6')
def web6():
    return render_template("web6.html")

@app.route('/web7')
def web7():
    return render_template("web7.html")

@app.route('/web8')
def web8():
    return render_template("web8.html")

@app.route('/web9')
def web9():
    return render_template("web9.html")

@app.route('/web10')
def web10():
    return render_template("web10.html")

@app.route('/web11')
def web11():
    return render_template("web11.html")

@app.route('/web12')
def web12():
    return render_template("web12.html")

@app.route('/web13')
def web13():
    return render_template("web13.html")

@app.route('/web14')
def web14():
    return render_template("web14.html")

@app.route('/web15')
def web15():
    return render_template("web15.html")

if __name__ == "__main__":
    app.run(debug=True)
