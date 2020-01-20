from flask import request
from flask_restplus import Namespace, Resource, fields

from rpsls_api.commons import constants, choice_helper
from rpsls_api.models import Scoreboard
from rpsls_api.extensions import db

api = Namespace('rpsls', description='RPSLS related operations')


user_choice_field = api.model('UserChoiceField', {
    'player': fields.Integer(required=True, description='Player Choice ID')
})


@api.route("/play")
class PlayResource(Resource):
    @api.expect(user_choice_field, validate=True)
    def post(self):
        body = request.get_json()
        user_choice_id = body.get('player')

        try:
            comp_choice = choice_helper.generate_computer_choice()
        except Exception as e:
            return {"error": "error generating computer choice. Reason{}".format(e.args)}, 400

        # another idea is to store combinations of choices with what they can beat
        # e.g {spock: ['scissor', 'rock']}
        # if user_choice == spock tie, else if user_choice in spock, user loses, else user wins

        d = (user_choice_id - comp_choice + 5) % 5

        if d == 0:
            results = "tie"
            message = "Its a tie!" + " You chose " + constants.POSSIBLE_CHOICES.get(user_choice_id) + \
                      ". Computer chose " + constants.POSSIBLE_CHOICES.get(comp_choice)
        elif d in [1, 3]:
            results = "win"
            message = "You win!" + " You chose " + constants.POSSIBLE_CHOICES.get(user_choice_id) + \
                      ". Computer chose " + constants.POSSIBLE_CHOICES.get(comp_choice)
        else:
            results = "lose"
            message = "You lose!" + " You chose " + constants.POSSIBLE_CHOICES.get(user_choice_id) + \
                      ". Computer chose " + constants.POSSIBLE_CHOICES.get(comp_choice)

        return {
            "results": results,
            "player": user_choice_id,
            "computer": comp_choice,
            "message": message
        }


@api.route("/choice")
class RandomChoiceResource(Resource):
    def get(self):
        comp_choice = choice_helper.generate_computer_choice()
        return {
            "id": comp_choice,
            "name": constants.POSSIBLE_CHOICES.get(comp_choice)
        }


@api.route("/choices")
class ChoicesResource(Resource):
    def get(self):
        choices = []
        for k, v in constants.POSSIBLE_CHOICES.items():
            choices.append({
                "id": k,
                "name": v
            })

        return choices
