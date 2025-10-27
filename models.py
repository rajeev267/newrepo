from extensions import db


class Student(db.Model):
    roll_no = db.Column(db.String(11), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    batch = db.Column(db.String(20), nullable=False)
    branch= db.Column(db.String(50), nullable=True)
    def __repr__(self):
        return f"<Student {self.name}>"


class teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username= db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class SubjectMarks(db.Model):
    __tablename__ = 'subject_marks'

    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(100), nullable=False)

    # 10 test marks
    test1 = db.Column(db.Float)
    test2 = db.Column(db.Float)
    test3 = db.Column(db.Float)
    test4 = db.Column(db.Float)
    test5 = db.Column(db.Float)
    test6 = db.Column(db.Float)
    test7 = db.Column(db.Float)
    test8 = db.Column(db.Float)
    test9 = db.Column(db.Float)
    test10 = db.Column(db.Float)

    # foreign key reference to Student table
    roll_no = db.Column(db.String(11), db.ForeignKey('student.roll_no'), nullable=False)

    # relationship for easy access
    student = db.relationship('Student', backref='subject_marks')
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)


