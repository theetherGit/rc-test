from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_Key'] = '448510c83202155ff4a5cb42930d83750384b6da'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {
    'db1': 'mysql+pymysql://root:root@localhost:3306/Test',
    #'db-post': 'postgresql://root:root@localhost:5432/Test',
    'db2': SQLALCHEMY_DATABASE_URI
}

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__: 'person_sql'
    __bind_key__: 'db1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dob =db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'Name => {self.name} and DOB => {self.dob}'

class Employee(db.Model):
    __tablename__: 'Employee Details'
    __bind_key__: 'db2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dob =db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'Name => {self.name} and DOB => {self.dob}'


@app.route('/mysql')
def index():
    '''person = Person(name="Ether", address="delhi", dob="2001")
    db.session.add(person)
    db.session.commit()'''
    person = Person.query.all()
    print(person)
    return 'Response done for MySQL check terminal'

@app.route('/postgresql')
def pindex():
    '''person = Employee(name="Ether", address="delhi", dob="2001")
    db.session.add(person)
    db.session.commit()'''
    person = Employee.query.all()
    print(person)
    return 'Response Done for Postgresql check terminal'

if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
