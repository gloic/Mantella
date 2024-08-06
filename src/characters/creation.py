import llm
import prompts_fr as prompts
from character import Character


def create_character(character: Character):
    print(f"Processing character : {character.get_name()} - {character.get_race()} - {character.get_gender()} - {character.get_species()}")
    prompt = prompts.user_prompt_character_writer.format(
        name=character.get_name(),
        race=character.get_race(),
        species=character.get_species(),
        gender=character.get_gender(),
        bio=character.get_bio()
    )

    new_prompt = llm.generate(system_prompt=prompts.system_prompt_character_writer, prompt=prompt)
    character.set_new_prompt(new_prompt)
    return character
