from rpsls_api.extensions import db
from sqlalchemy import UniqueConstraint
import time

class Scoreboard(db.Model):
    __tablename__ = "scoreboard"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    win = db.Column(db.Boolean())
    lose = db.Column(db.Boolean())
    tie = db.Column(db.Boolean())
    create_time = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Scoreboard, self).__init__(**kwargs)
        self.create_time = int(time.time())
