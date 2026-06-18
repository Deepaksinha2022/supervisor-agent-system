from app.prompts.prompt_registry import PROMPT_VERSION


def log_prompt_version(agent_name: str):

    print(
        f"[{agent_name}] Prompt Version: {PROMPT_VERSION}"
    )