from flask import Flask, render_template, url_for, redirect, request
from forms import AdminRegistration, AdminLogin, Survey
from flask_socketio import SocketIO, send
import FindingSocialMedia as fsm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8dbfc8e2eccbaae955fca015c647d5eb'

socketio = SocketIO(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/social-media-suggestions")
def suggestion():
    first = request.values.get('first')
    second = request.values.get('second')
    third = request.values.get('third')
    return render_template("social-media-suggestions.html", first=first, second=second, third=third)

@app.route("/<social_media_name>")
def tutorial(social_media_name):
    return render_template(social_media_name + ".html")

@app.route("/survey", methods=['GET', 'POST'])
def survey():
    form = Survey()
    # suggestions = fsm.similar(form)
    if form.validate_on_submit():

        family = float(form.family.data)
        pictures = float(form.pictures.data)
        videos = float(form.videos.data)
        world_communities = float(form.world_communities.data)
        varied_communities = float(form.varied_communities.data)
        news = float(form.news.data)
        celebrities = float(form.celebrities.data)
        long_form = float(form.long_form.data)

        attributes = [family, pictures, videos, world_communities, varied_communities, news, celebrities, long_form]

        suggestions = fsm.similar(attributes)

        return redirect(url_for('suggestion', first=suggestions[0], second=suggestions[1], third=suggestions[2]))
    return render_template('survey.html', title='Survey', form=form)



@app.route('/chatbox')
def chatbox():
    return render_template('chatbox.html', title='Chatbox')

def message_received(methods=['GET', 'POST']):
    print("Message was received!")

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@app.route("/admin-register", methods=['GET', 'POST'])
def admin_register():
    form = AdminRegistration()
    return render_template('admin-register.html', title='Admin Register', form=form)

@app.route('/admin-login')
def admin_login():
    form = AdminLogin()
    return render_template('admin-login.html', title='Admin Login', form=form)


if __name__ == "__main__":
    socketio.run(app, debug=True)