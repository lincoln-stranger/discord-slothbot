import json
import random


def load_sloth_facts(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        return data["facts"]


def get_random_fact(facts):
    return random.choice(facts)
