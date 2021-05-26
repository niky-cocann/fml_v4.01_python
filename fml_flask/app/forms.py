from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, DecimalField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ConfigForm(FlaskForm):
    normal_display_brightness = DecimalField('Display Brightness (Normal Operating Mode)', places=0, validators=[NumberRange(10, 90, "Display Brightness must take values between 0 and 100, inclusive"), DataRequired()])
    active_display_brightness = DecimalField('Display Brightness (Active Operating Mode)', places=0, validators=[NumberRange(10, 90, "Display Brightness must take values between 0 and 100, inclusive"), DataRequired()])
    active_display_brightness_duration = StringField('Active Display Brightness Duration', validators=[DataRequired()])
    fuel_display_duration = StringField('Fuel Display Duration', validators=[DataRequired()])
    refill_display_duration = StringField('Refill Display Duration', validators=[DataRequired()])
    flow_encoder_ratio = StringField('Flow Encoder Ratio', validators=[DataRequired()])
    debounce_time_reed = StringField('Debounce Time (Reed)', validators=[DataRequired()])
    debounce_time_hall = StringField('Debounce Time (Hall)', validators=[DataRequired()])
    run_out_duration = StringField('Run Out Duration', validators=[DataRequired()])
    run_out_level = StringField('Run Out Level', validators=[DataRequired()])

    submit = SubmitField('Save Configuration')


class TankForm(FlaskForm):
    file = FileField('Upload e new tank configuration file', validators=[FileRequired()])

    submit = SubmitField('Upload file')

