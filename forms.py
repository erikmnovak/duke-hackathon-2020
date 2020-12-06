from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired

class AdminRegistration(FlaskForm):
    username = StringField('username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    confirm_email = StringField('Email', 
                                validators=[DataRequired(), EqualTo('email')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Finish registration')

class AdminLogin(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')

class Survey(FlaskForm):

    importance = {"Not important at all" : 0,
                   "Slightly important" : 1,
                   "Somewhat important" : 2,
                   "Very important" : 3,
                   "The most important": 4}

    options = [(value, key) for (key, value) in importance.items()]

    family = RadioField('Being able to connect with family members.', choices=options, validators=[InputRequired()])
    pictures = RadioField('Being able to share and see pictures.', choices=options, validators=[InputRequired()])
    videos = RadioField('Being able to share and watch videos.', choices=options, validators=[InputRequired()])
    world_communities = RadioField(' Being able to connect with communities from all around the world', choices=options, validators=[InputRequired()])
    varied_communities = RadioField('Being able to engage in social discourse in varied communities.', choices=options, validators=[InputRequired()])
    news = RadioField('Being able to receive up to date news from various sources.', choices=options, validators=[InputRequired()])
    celebrities = RadioField('Being able to follow celebrities or important people.', choices=options, validators=[InputRequired()])
    long_form = RadioField('Having a focus on longer content as opposed to shorter content.', choices=options, validators=[InputRequired()])

    submit = SubmitField('Find out!')