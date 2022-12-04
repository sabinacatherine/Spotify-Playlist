
#key imports for building a flask form
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#initial form setup,initializing Flask app

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'not_so_secret_key'

# Flask-Bootstrap requires this line
Bootstrap(app)

#form control configs here
class SongForm(FlaskForm):
    song_input_field = StringField('What is your favourite song?', validators=[DataRequired()])
    submit_field = SubmitField('Submit')


# all Flask routes below

@app.route('/', methods=['GET', 'POST'])
def index():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = SongForm()
    message = ""
    if form.validate_on_submit():
        name = form.song_input_field.data
        if song_name in pt_concat['SName']:
            # empty the form field
            form.song_input_field.data = ""
            # redirect the browser to another route and template
            return redirect(url_for('song'))
        else:
            message = "That song is not in our database."
    return render_template('index.html', names=names, form=form, message=message)

@app.route('/song')
def playlist(song_name):
    # run function to get playlist data
    playlist = get_playlist(song_name)
    if song_name == "Unknown":
        # redirect the browser to the error template
        return render_template('404.html'), 404
    else:
        # pass all the data for the selected actor to the template
        return render_template('song.html', playlist = playlist)

# 2 routes to handle errors - they have templates too

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
