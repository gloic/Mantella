from character import Character
from llm import Llm


class Creation:
    def __init__(self, params=None, llm: Llm = None):
        self.params = params or {}
        self.system_prompt_character_writer = self.params.get('system_prompt_character_writer2', None)
        self.user_prompt_character_writer = self.params.get('user_prompt_character_writer', None)

        self.llm = llm

    def create_character(self, character: Character):
        print(f"Processing character : {character.get_name()} - {character.get_race()} - {character.get_gender()} - {character.get_species()}")
        prompt = self.user_prompt_character_writer.format(
            name=character.get_name(),
            race=character.get_race(),
            species=character.get_species(),
            gender=character.get_gender(),
            bio=character.get_bio()
        )

        new_prompt = self.llm.generate(system_prompt=self.system_prompt_character_writer, prompt=prompt)
        character.set_new_prompt(new_prompt)
        return character
