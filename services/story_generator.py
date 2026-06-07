from services.prompt_builder import build_prompt
from services.slm_service import ask_slm


def ask_dataset(
    df,
    question
):

    prompt = build_prompt(
        df,
        question
    )

    return ask_slm(prompt)