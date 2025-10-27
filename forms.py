from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired, Optional

# ===== Login Form =====
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# ===== Add Student Form =====
class AddStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    roll_no = StringField('Roll No', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    dob = StringField('DOB', validators=[DataRequired()])
    father_name = StringField('Father Name', validators=[DataRequired()])
    mother_name = StringField('Mother Name', validators=[DataRequired()])
    mobile = StringField('Mobile', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    batch = IntegerField('Batch', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    branch = StringField('Branch', validators=[DataRequired()])
    submit = SubmitField('Add Student')


# ===== Add Teacher Form =====
class AddTeacherForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add Teacher')


# ===== Change Password Form =====
class ChangePasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Change Password')

# ===== Modify Student Data Form =====
class ModifyStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    father_name = StringField('Father Name', validators=[DataRequired()])
    mother_name = StringField('Mother Name', validators=[DataRequired()])
    dob = StringField('DOB', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    mobile = StringField('Mobile', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    batch = IntegerField('Batch', validators=[DataRequired()])
    submit = SubmitField('Modify Student Data')
# ===== Subject Marks Form =====
class AddMarksForm(FlaskForm):
    roll_no = StringField('Roll No', validators=[DataRequired()])
    subject_name = StringField('Subject Name', validators=[DataRequired()])
    test1 = FloatField('Test 1', validators=[Optional()])
    test2 = FloatField('Test 2', validators=[Optional()])
    test3 = FloatField('Test 3', validators=[Optional()])
    test4 = FloatField('Test 4', validators=[Optional()])
    test5 = FloatField('Test 5', validators=[Optional()])
    test6 = FloatField('Test 6', validators=[Optional()])
    test7 = FloatField('Test 7', validators=[Optional()])
    test8 = FloatField('Test 8', validators=[Optional()])
    test9 = FloatField('Test 9', validators=[Optional()])
    test10 = FloatField('Test 10', validators=[Optional()])
    submit = SubmitField('Save Marks')




class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit Feedback')
