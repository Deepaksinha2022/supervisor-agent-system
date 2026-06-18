import hashlib

from app.prompts.research_prompt import RESEARCH_PROMPT

from app.prompts.research_prompt_v2 import RESEARCH_PROMPT_V2


PROMPT_VERSION = hashlib.md5(
    RESEARCH_PROMPT.encode()
).hexdigest()[:8]

PROMPT_VERSION_V2 = hashlib.md5(
    RESEARCH_PROMPT_V2.encode()
).hexdigest()[:8]