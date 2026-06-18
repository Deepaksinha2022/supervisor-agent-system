import hashlib

from app.prompts.research_prompt import RESEARCH_PROMPT


PROMPT_VERSION = hashlib.md5(
    RESEARCH_PROMPT.encode()
).hexdigest()[:8]