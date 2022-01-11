from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ###
    courseName = db.Column(db.String(100))
    totalScore = db.Column(db.Integer)
    letterGrade = db.Column(db.String(10))
    exam = db.Column(db.Integer)
    ca = db.Column(db.Integer)
    ####
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class SemesterGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ###
    courseName = db.Column(db.String(100))
    courseTitle = db.Column(db.String(1000))
    year = db.Column(db.Integer)
    semester = db.Column(db.String(10))
    score = db.Column(db.Integer)
    grade = db.Column(db.String(10))
    gpa = db.Column(db.String(10))
    tcu = db.Column(db.String(10))
    ####
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    matriculationNumber = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
    semesterGrades = db.relationship('SemesterGrade')