from app.prompts.prompt_registry import (
    PROMPT_VERSION,
    PROMPT_VERSION_V2
)


def log_prompt_version(
    agent_name: str,
    variant: str
):

    version = (
        PROMPT_VERSION_V2
        if variant == "v2"
        else PROMPT_VERSION
    )

    print(
        f"[{agent_name}] Variant: {variant} | Prompt Version: {version}"
    )