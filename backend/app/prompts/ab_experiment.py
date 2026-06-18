from app.prompts.ab_router import choose_prompt


def get_prompt_variant():

    variant = choose_prompt()

    print(
        f"AB_TEST_VARIANT={variant}"
    )

    return variant