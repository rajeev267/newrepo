from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os

from forms import LoginForm, AddStudentForm, ChangePasswordForm,AddTeacherForm, AddMarksForm, ModifyStudentForm, FeedbackForm
from extensions import db
from models import Student, teachers, SubjectMarks, Feedback

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# if os.environ.get('FLASK_ENV') == 'development':
#     # Local development: SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Cse.db'
# else:
#     # Production / Deployment: PostgreSQL
#     # Format: postgresql://username:password@host:port/database
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#         'DATABASE_URL', 
#         'postgresql://cse_user:yourpassword@localhost:5432/cse_db'
    # )

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)




# ===== Routes =====

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    return render_template('contect.html')
@app.route('/lab')
def lab():  
    return render_template('lab.html')



@app.route('/student_login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if username exists
        user = Student.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            
            subject_marks = SubjectMarks.query.filter_by(roll_no=user.roll_no).all()

            flash('Login successful!', 'success')
            return render_template(
                'student_deshboard.html',
                user=user,
                subject_marks=subject_marks
            )

        flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

@app.route('/teacher_login', methods=['GET', 'POST'])
def teacher_login():
    special_users = {
        'admin': 'adminpass'
    }

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check for special users
        if username in special_users and special_users[username] == password:
            flash('Login successful!', 'success')
            return render_template('admin_deshboard.html', username=username)
        # Teacher login
        user = teachers.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return render_template('teacher_dashboard.html', user=user)
        flash('Invalid username or password', 'danger')
    return render_template('teacher_login.html', form=form)








@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():  
    form = AddTeacherForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        new_teacher = teachers(  
            username=form.username.data,
            name=form.name.data,
            password=hashed_password,
        )

        db.session.add(new_teacher)
        db.session.commit()
        flash('Teacher added successfully!', 'success')
        return redirect(url_for('teacher_login'))

    return render_template('add_teacher.html', form=form)





@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        new_student = Student(
            username=form.username.data,
            name=form.name.data,
            password=hashed_password,
            father_name=form.father_name.data,
            mother_name=form.mother_name.data,
            dob=form.dob.data,
            age=form.age.data,
            year=form.year.data,
            mobile=form.mobile.data,
            email=form.email.data,
            batch=form.batch.data,
            branch=form.branch.data,
            roll_no=form.roll_no.data
        )

        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('add_student.html', form=form)


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        username = form.username.data
        old_password = form.old_password.data
        new_password = form.new_password.data

        user = Student.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, old_password):
            user.password = generate_password_hash(new_password)
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('login'))

        flash('Invalid username or old password', 'danger')

    return render_template('change_password.html', form=form)
@app.route('/students')
def student_list():
    # Get filter values from query parameters (URL)
    roll_no = request.args.get('roll_no', '').strip()
    year = request.args.get('year', '').strip()
    batch = request.args.get('batch', '').strip()
    father_name = request.args.get('father_name', '').strip()

    # Start the query with only selected columns
    query = Student.query.with_entities(
        Student.name,
        Student.roll_no,
        Student.year,
        Student.batch,
        Student.father_name
    )

    # Apply filters dynamically (only if user entered something)
    if roll_no:
        query = query.filter(Student.roll_no.ilike(f"%{roll_no}%"))
    if year:
        query = query.filter(Student.year == year)
    if batch:
        query = query.filter(Student.batch.ilike(f"%{batch}%"))
    if father_name:
        query = query.filter(Student.father_name.ilike(f"%{father_name}%"))

    # Execute the query
    students = query.all()

    # Send data to template
    return render_template(
        'student_list.html',
        students=students,
        roll_no=roll_no,
        year=year,
        batch=batch,
        father_name=father_name
    )


@app.route('/logout')
def logout():
    return redirect(url_for('home'))
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# modify data of student
@app.route('/edit_student', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = AddStudentForm(obj=student)

    if form.validate_on_submit():
        student.username = form.username.data
        student.name = form.name.data
        student.father_name = form.father_name.data
        student.mother_name = form.mother_name.data
        student.dob = form.dob.data
        student.age = form.age.data
        student.year = form.year.data
        student.mobile = form.mobile.data
        student.email = form.email.data
        student.batch = form.batch.data

        db.session.commit()
        flash('Student details updated successfully!', 'success')
        return redirect(url_for('teacher_dashboard'))

    return render_template('edit_student.html', form=form, student=student)

@app.route('/add_marks', methods=['GET', 'POST'])
def add_marks():
    form = AddMarksForm()

    if form.validate_on_submit():
        # Check if student exists
        student = Student.query.filter_by(roll_no=form.roll_no.data).first()
        if not student:
            flash(f"Student with roll number {form.roll_no.data} not found!", "error")
            return redirect('/add_marks')

        # Check if record for this subject exists
        record = SubjectMarks.query.filter_by(
            roll_no=form.roll_no.data,
            subject_name=form.subject_name.data
        ).first()

        if not record:
           
            record = SubjectMarks(
                roll_no=form.roll_no.data,
                subject_name=form.subject_name.data
            )
            db.session.add(record)

        for i in range(1, 11):
            value = getattr(form, f'test{i}').data
            if value is not None:
                setattr(record, f'test{i}', value)

        db.session.commit()

        if record.id:
            flash("Marks added or updated successfully!", "success")
        else:
            flash("New record created successfully!", "success")

        return redirect('/add_marks')

    return render_template('add_marks.html', form=form)

# add marks dinamacily if needed

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()  
    if form.validate_on_submit():
        new_feedback = Feedback(  
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(new_feedback)
        db.session.commit()
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('feedback.html', form=form)

@app.route('/view_feedbacks')
def view_feedbacks():
    feedbacks = Feedback.query.all()
    return render_template('view_feedbacks.html', feedbacks=feedbacks)

     


# ===== Run app =====
if __name__ == '__main__':
    # Create tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
