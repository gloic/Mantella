import os

import pandas as pd

import llm
import translation
import evaluation

os.environ["no_proxy"] = "ldllmedt1,localhost,127.0.0.1,::1"


system_prompt_character_writer = """Créez une personnalité unique et captivante pour ce personnage, en vous inspirant de ses antécédents et de son histoire, tels que décrits dans le wiki du jeu. 
Concentrez-vous sur ses traits de caractère, son humeur et sa backstory, tout en ignorant délibérément toute information relative à son apparence physique, car celle-ci est non pertinente pour les interactions. 
Écrivez le prompt à la deuxième personne du singulier, en utilisant une longueur d'un ou deux paragraphes, et assurez-vous qu'il reflète fidèlement la personnalité et l'histoire du personnage.

- Ne jamais mentionner le jeu vidéo
- La langue utilisée est toujours le français.
"""

system_prompt_character_mantella = """
"""

system_prompt_character_evaluation = """
"""


# system_prompt_character_writer = """Rédige un prompt correspondant à un personnage du jeu Skyrim.
# Notes et instructions :
# - Certaines informations du personnage sont issues du wiki du jeu, elle peuvent contenir des informations non pertinentes qui ne doivent pas être utilisées. Il est important de s'inspirer de ces informations sans les réutiliser telles quelles..
# - ne pas inclure de citation du personnage
# - rédiger une personnalité unique et taillée sur mesure à ce personnage, il est possible d'ajouter des traits de caractères ou une humeur
# - important : il est interdit de décrire l'aspect physique du personnage, cette information est non pertinente pour dialoguer
#
# Rédige le prompt d'une longueur de 1 ou 2 paragraphes le plus crédible et cohérent par rapport au personnage.
#
# Le prompt s'adresse au personnage à jouer il faut écrire à la 2eme personne du singulier. Exemple : "Tu es (nom), un orc qui a grandi au nord de Bordeciel..."
# La langue utilisée est toujours le français.
# """




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
    character_prompt = llm.generate(system_prompt_character_writer, prompt)

    print(character_prompt)
    evaluation.evaluate(name, character_prompt)


    if i > 2:
        break
