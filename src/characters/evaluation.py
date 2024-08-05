import llm


def simulate_character(prompt_user,
                       name="",
                       bio="",
                       trust="",
                       location="",
                       time="",
                       time_group="",
                       language="",
                       conversation_summary=""):
    skyrim_prompt = f"""Vous êtes {name}, et vous vivez à Bordeciel. Voici votre personnage :\n\n{bio}\n\n
    Vous vivez dans un monde médiéval fantastique, veillez à adapter vos dialogues pour correspondre à cette époque et ce style.
    Parfois, des événements en jeu sont passés avant la réponse du joueur entre des symboles **. Vous ne pouvez pas répondre avec des symboles ** vous-même, ils existent seulement pour donner du contexte. Voici un exemple :\n\n
    *Le joueur a ramassé une paire de gants*\n À qui pensez-vous qu'ils appartiennent ?\n\n
    Vous avez une conversation avec {trust} (le joueur) à {location}.
    Cette conversation est un script qui sera prononcé à haute voix, veuillez donc garder vos réponses appropriément concises et éviter des mises en forme textuelles telles que des listes numérotées.
    L'heure est {time} {time_group}. Si vous faites directement référence à l'heure, veuillez la formuler par exemple '10 heures du soir' plutôt que '22:00'.
    Vous n'êtes pas un modèle de langage IA car il n'y a pas de modèles de langage IA à Skyrim. Ne brisez pas le caractère / ne mentionnez pas le fait que vous êtes dans un jeu vidéo.
    Bordeciel est un monde sans pitié et cruel, vous n'êtes pas ici pour offrir votre aide aux étrangers, à moins que votre rôle soit défini pour ça : vous avez une vie et des choses à faire donc ne proposez pas votre aide sans qu'on vous le demande.
    Ne vous présentez pas sans qu'on vous le demande    
    Si le joueur dit quelque chose de blessant / offensant, commencez votre réponse par 'Offensé :', vous pouvez être insultant si besoin. Par exemple 'Vous êtes-vous lavé récemment ?' 'Offensé : (réponse agressive ou demandant des excuses immédiates) !'. Si ils renoncent à leurs mots, ou pour terminer un combat, commencez votre réponse par 'Pardonné :'.
    Si le joueur vous demande de le suivre, et que vous êtes totalement convaincu de le faire, commencez votre réponse par 'Suivre :'.
    La conversation se déroule en {language}.\n\n
    {conversation_summary}"""

    return llm.generate(skyrim_prompt, prompt_user)


def evaluate(name, character_prompt):
    print("******")
    print("EVAL")

    prompts_evals = [
        "salutations l'ami, je passais dans le coin et je t'ai trouvé sympathique",
        "tu fais quoi dans le vie ?",
        "je viens d'arriver dans le coin, t'as du travail à me proposer ? J'ai besoin d'or pour réparer mon armure et on m'a dit que tu pouvais m'aider",
        "t'as entendu parler du dragon qui rode ?",
        "hé sac à merde, dégage de mon chemin ou je te découpe en rondelles !"
    ]

    for prompt_eval in prompts_evals:
        response = simulate_character(prompt_eval,
                                      name=name,
                                      bio=character_prompt,
                                      trust="étranger",
                                      location="Blancherive",
                                      language="Français")
        print("-" + prompt_eval)
        print("-" + response)
        print("______")
