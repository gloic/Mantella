import llm
import prompts_fr as prompts
from character import Character


def generate_conversation(character: Character, user_prompts):
    # def get_history_entry(role, content):
    #     return {"role": role, "content": content}

    get_history_entry = lambda role, content: {"role": role, "content": content}

    system_prompt = prompts.system_prompt_character_skyrim.format(
        name=character.get_name(),
        bio=character.get_new_prompt(),
        trust="étranger",
        location="Blancherive",
        language="French",
        time="10:04",
        time_group="",
        conversation_summary=""
    )

    history = [get_history_entry("system", system_prompt)]

    for user_prompt in user_prompts:
        if user_prompt is not None:
            print(" - user: " + user_prompt)
            history.append(get_history_entry("user", user_prompt))

        response = llm.generate(history, temperature=1, top_p=0.9)

        print(" - assistant: " + response)
        history.append(get_history_entry("assistant", response))

    return history


def evaluate(character: Character):
    print("******")
    print("SIMULATION")
    print("******")

    for user_prompts in prompts.prompts_evals:

        history = []
        for chat in generate_conversation(character, user_prompts):
            history.append("-{role}: {content}".format(role=chat["role"],
                                                       content=chat["content"]))

        print("> Evaluation")

        response_eval = llm.generate(system_prompt=prompts.system_prompt_character_evaluation,
                                     prompt=prompts.user_prompt_character_evaluation.format(bio=character.get_new_prompt(), chat_history=history),
                                     temperature=0.9,
                                     top_p=0.8)

        print(response_eval)
        print("______")
