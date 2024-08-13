import argparse
import json
import os
from os.path import join

import pandas as pd

from llm import Llm
from evaluation import Evaluation
from character import Character
from creation import Creation

os.environ["no_proxy"] = "192.168.0.10,ldllmedt1,localhost,127.0.0.1,::1"

data = pd.read_csv('resources/skyrim_characters_fr.csv')


def load_config(config_file):
    with open(config_file, "r") as file:
        json_data = json.load(file)
    return json_data


def run_process(config):
    llm_params = config.get("llm", {}).get("params", {})
    creation_params = config.get("creation", {}).get("params", {})
    eval_params = config.get("evaluation", {}).get("params", {})

    llm = Llm(llm_params)
    creation = Creation(creation_params, llm)
    evaluation = Evaluation(eval_params, llm)

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aria.")
    parser.add_argument("--config", default="default.json", help="Path to JSON config file in the configs folder")
    args = parser.parse_args()

    config_path = join("configs", args.config)
    config = load_config(config_path)

    run_process(config)
