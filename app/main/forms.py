from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms import validators
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you:',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
  title = StringField(' title:',validators=[DataRequired()]) 
  post = StringField(' post:',validators=[DataRequired()]) 
  username= StringField(' username:',validators=[DataRequired()])
  category = SelectField("Choose your desired category:",choices=[('Business','Business'),('Fashion','Fashion'),('Education','Education'),('Humour','Humour'),('Sports','Sports')])

  submit = SubmitField('Submit')


class CommentForm(FlaskForm):
  comment = TextAreaField('Add a Comment:',validators=[DataRequired()])
  submit = SubmitField('Submit') 