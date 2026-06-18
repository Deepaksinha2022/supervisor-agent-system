import random

def choose_prompt():

    if random.random() < 0.2:
        return "v2"

    return "v1"