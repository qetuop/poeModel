from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = None
db = SQLAlchemy()
config = None

#app = Flask(__name__)
#app.config.from_object(Config)


def setup(_app=None, _db=None, _config=None):
    global app, db

    if _app is None:
        app = Flask(__name__)
    else:
        app = _app

    if _config is None:
        app.config.from_object(Config)
    else:
        app.config.from_object(_config)

    if _db is None:
        db = SQLAlchemy(app)
    else:
        db = _db


class Item(db.Model):
    print('here')
    id = db.Column(db.Integer, primary_key=True)
    verified = db.Column(db.Boolean)
    properties = db.relationship('Property', backref='item', lazy='dynamic')


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    name = db.Column(db.String(128))

'''
    def __init__(self, ascendancyClass, class_, classId, experience, lastActive, league, level, name):
        self.ascendancyClass = ascendancyClass
        self.class_ = class_   #fck
        self.classId = classId
        self.experience = experience
        self.lastActive = lastActive
        self.league = league
        self.level = level
        self.name = name
        
        {'character': {'ascendancyClass': 2, 'class': 'Trickster', 'classId': 6, 'experience': 2182014614, 'lastActive': True, 'league': 'Blight', 'level': 91, 'name': 'SalWrendMkII'}
        '''
class CharacterInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ascendancy_class = db.Column(db.String(32))
    class_ = db.Column(db.String(32))
    class_id = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    last_active = db.Column(db.Boolean)
    league = db.Column(db.String(32))
    level = db.Column(db.Integer)
    name = db.Column(db.String(128))


if __name__ == '__main__':
    print('there')
    setup()

    db.drop_all()
    db.create_all()

    dbItem = CharacterInfo(ascendancy_class='fpp')
    db.session.add(dbItem)


    db.session.commit()



