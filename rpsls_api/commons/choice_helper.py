import requests
import json


def generate_computer_choice():
    response = requests.get('https://codechallenge.boohma.com/random', verify=False)
    random_num = json.loads(response.text).get("random_number") / 20
    print(random_num)
    if random_num <= 1:
        return 1
    elif random_num <= 2:
        return 2
    elif random_num <= 3:
        return 3
    elif random_num <= 4:
        return 4
    elif random_num <= 5:
        return 5
