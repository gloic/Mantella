import llm
import prompts_fr as prompts


def simulate_character(prompt_user,
                       name="",
                       bio="",
                       trust="",
                       location="",
                       time="",
                       time_group="",
                       language="",
                       conversation_summary=""):
    prompt = prompts.system_prompt_character_skyrim.format(
        name=name,
        bio=bio,
        trust=trust,
        location=location,
        time=time,
        time_group=time_group,
        language=language,
        conversation_summary=conversation_summary
    )
    return llm.generate(system_prompt=prompt, prompt=prompt_user)


def evaluate(name, character_prompt):
    print("******")
    print("SIMULATION")
    print("******")

    prompts_evals = [
        "salutations l'ami, je passais dans le coin et je t'ai trouvé sympathique, tu sais où se trouve l'auberge la plus proche ? J'te paie un hydromel !",
        "tu fais quoi dans le vie ?",
        "je viens d'arriver dans le coin et j'ai besoin d'or pour réparer mon armure. On m'a dit que tu pouvais m'aider, est-ce que t'as du travail à me proposer ?",
        "t'as entendu parler du dragon qui rode ?",
        "j'ai un travail bien payé à te proposer, c'est pas dangereux mais pas très légal. Alors ça te tente quelques pièces d'or ?",
        "hé sac à merde, dégage de mon chemin ou je te découpe en rondelles !"
    ]

    for prompt_eval in prompts_evals:
        response = simulate_character(prompt_eval,
                                      name=name,
                                      bio=character_prompt,
                                      trust="étranger",
                                      location="Blancherive",
                                      language="Français")
        print("Sample : ")
        print(" - " + prompt_eval)
        print(" - " + response)
        print("______")

        messages = [
            {"role": "system", "content": prompts.system_prompt_character_evaluation},
            {"role": "user", "content": prompt_eval},
            {"role": "assistant", "content": response},
        ]

        print("> Evaluation")
        response_eval = llm.generate(messages=messages,
                                     temperature=0.4,
                                     top_p=0.4)

        print(response_eval)


        # messages.append({"role": "assistant", "content": response_eval})
        # messages.append({"role": "user", "content": prompts.system_prompt_character_evaluation_2})
        # response_final_eval = llm.generate(messages=messages,
        #                              temperature=0.4,
        #                              top_p=0.4)
        # print("Final eval: " + response_final_eval)
        print("______")
