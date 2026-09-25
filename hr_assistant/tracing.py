"""
LangSmith tracing needs no wiring in our own code - LangChain looks for LANGSMITH_TRACING,
LANGSMITH_ENDPOINT, LANGSMITH_API_KEY, LANGSMITH_PROJECT, directly in the environment (loaded from
.env by config.py) and if tracing is turned on, automatically sends a trace of every LLM call, tool call, and
agent step to your LangSmith project.

This module doesn't turn tracing on - te env vars already do that. ALl it does is log, once per run, whether
tracing is active, so it's obvious from the logs whether this run was traced.
"""
from hr_assistant import config
from hr_assistant.logger import get_logger
logger = get_logger(__name__)

def check_langsmith_tracing() -> None:
    """Log whether langsmith tracing is enabled for this run"""
    tracing_on = config.LANGSMITH_TRACING.lower() == "true"
    if tracing_on and config.LANGSMITH_API_KEY:
        logger.info(f"LangSmith tracing enabled: project - {config.LANGSMITH_PROJECT}, traces at https://langsmith.com")

    else:
        logger.info("Langsmith tracing disabled (set LANGSMITH_TRACING to true in .env file")
