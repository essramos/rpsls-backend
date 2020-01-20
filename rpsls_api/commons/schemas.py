from rpsls_api.extensions import ma, db
from rpsls_api.models import Scoreboard


class ScoreboardSchema(ma.ModelSchema):
    class Meta:
        model = Scoreboard
        sqla_session = db.session
