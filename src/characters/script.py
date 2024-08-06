import os

import pandas as pd

import creation
import evaluation

import translation
from character import Character

os.environ["no_proxy"] = "ldllmedt1,localhost,127.0.0.1,::1"

data = pd.read_csv('resources/skyrim_characters_fr.csv')

i = 0
for i, row in data.sample(replace=True, frac=1).iterrows():
    print("*********")

    character_data = {
        'name': row['name'],
        'race': row['race'],
        'gender': row['gender'],
        'species': row['species'],
        'bio': row['bio']
    }

    character = Character(**character_data)
    character = creation.create_character(character)
    print(character.get_new_prompt())

    evaluation.evaluate(character)

    if i > 2:
        break
