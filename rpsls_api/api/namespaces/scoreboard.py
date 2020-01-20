from flask import request
from flask_restplus import Namespace, Resource, fields

from rpsls_api.commons import scoreboard_helper, schemas

from rpsls_api.models import Scoreboard
from rpsls_api.extensions import db

api = Namespace('scoreboard', description='Scoreboard related operations')


reset_scoreboard_fields = api.model('ResetScoreboardFields', {
    'username': fields.String(required=True)
})

scoreboard_fields = api.model('ScoreboardFields', {
    'username': fields.String(required=True),
    'result': fields.String(required=True, description="Result of a play")
})


@api.route("")
class ScoreboardResource(Resource):

    @api.expect(scoreboard_fields, validate=True)
    def post(self):
        """
        record play result
        """
        body = request.get_json()
        username = body.get("username")
        result = body.get("result")

        if result == "win":
            score = Scoreboard(
                username=username,
                win=1,
                lose=0,
                tie=0
            )
            db.session.add(score)
        elif result == "lose":
            score = Scoreboard(
                username=username,
                win=0,
                lose=1,
                tie=0
            )
            db.session.add(score)
        elif result == "tie":
            score = Scoreboard(
                username=username,
                win=0,
                lose=0,
                tie=1
            )
            db.session.add(score)
        else:
            return {"error": "Result not valid."}, 400           

        try:
            db.session.commit()
            return {"error": None}
        except Exception as e:
            db.session.rollback()
            return {"error": "Error recording this play. Reason {}".format(e.args)}, 400


@api.route("/stats")
class UserStatResource(Resource):

    query_parser = api.parser()
    query_parser.add_argument('username', required=True, location='args', type=str)

    @api.expect(query_parser, validate=True)
    def get(self, query_parser=query_parser):
        """
        returns win/lose/tie stat of a user
        """
        args = query_parser.parse_args()
        username = args['username']
        stats = scoreboard_helper.get_user_stats(username)
        if stats:
            return stats
        else:
            return {
                "win": 0,
                "lose": 0,
                "tie": 0
            }


@api.route("/list")
class ScoreboardListResource(Resource):

    query_parser = api.parser()
    query_parser.add_argument('username', required=True, location='args', type=str)
    query_parser.add_argument('limit', required=True, location='args', type=int)

    @api.expect(query_parser, validate=True)
    def get(self, query_parser=query_parser):
        """
        return most recent results
        """
        args = query_parser.parse_args()
        username = args['username']
        limit = args['limit']

        scoreboard_query = (
            Scoreboard.query.filter_by(username=username)
            .order_by(Scoreboard.create_time.desc())
            .limit(limit).all()
        )

        schema = schemas.ScoreboardSchema(many=True)

        return schema.dump(scoreboard_query).data

    @api.expect(reset_scoreboard_fields, validate=True)
    def delete(self):
        """
        deletes user play history
        """
        body = request.get_json()
        username = body.get("username")

        Scoreboard.query.filter_by(username=username).delete()

        try:
            db.session.commit()
            return {"error": None}
        except Exception as e:
            db.session.rollback()
            return {"error": "error resetting scoreboard. Reason {}".format(e.args)}, 400
