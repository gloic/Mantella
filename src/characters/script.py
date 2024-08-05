import os

import pandas as pd

import evaluation
import llm
import prompts_fr as prompts
import translation

os.environ["no_proxy"] = "ldllmedt1,localhost,127.0.0.1,::1"

data = pd.read_csv('resources/skyrim_characters_fr.csv')

i = 0
for i, row in data.sample(replace=True, frac=1).iterrows():
    print("*********")
    i = i + 1
    character = {
        'name': row['name'],
        'race': row['race'],
        'gender': row['gender'],
        'species': row['species'],
        'bio': row['bio']
    }

    name = character["name"]
    gender = translation.trad_gender(character["gender"])
    race = translation.trad_race(character["race"])
    species = translation.trad_species(character["species"])

    print(f"Processing character : {character['name']} - {character['race']} - {character['gender']} - {character['species']}")

    prompt = f"""
                Nom : {name}
                Race : {race}
                Espèce : {species}
                Genre : {gender}
                Informations de base du personnage : {character['bio']}                
            """
    character_prompt = llm.generate(system_prompt=prompts.system_prompt_character_writer,
                                    prompt=prompt)

    print(character_prompt)
    evaluation.evaluate(name, character_prompt)

    if i > 2:
        break
