from google.adk.agents import Agent
from . import prompt
from google.adk.tools import google_search

ideation_conversation_explorer_agent = Agent(
    name="ideation_conversation_explorer_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that introduces new angles, tangential connections, and unexpected insights that expand the conversation's scope."
    ),
    instruction=prompt.EXPLORER_PROMPT,
    tools=[google_search],
    output_key="explorer_input",
)
