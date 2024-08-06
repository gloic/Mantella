import translation


class Character:
    def __init__(self, name: str, race: str, gender: str, species: str, bio: str):
        self.__name = name
        self.__race = race
        self.__gender = gender
        self.__species = species
        self.__bio = bio
        self.__new_prompt = None
        self.translate()

    def translate(self):
        self.__race = translation.trad_race(self.__race)
        self.__gender = translation.trad_gender(self.__gender)
        self.__species = translation.trad_species(self.__species)

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_gender(self):
        return self.__gender

    def get_species(self):
        return self.__species

    def get_bio(self):
        return self.__bio

    def get_new_prompt(self):
        return self.__new_prompt

    def set_new_prompt(self, value):
        self.__new_prompt = value
