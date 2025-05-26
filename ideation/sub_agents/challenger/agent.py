from google.adk.agents import Agent
from . import prompt

ideation_conversation_challenger_agent = Agent(
    name="ideation_conversation_challenger_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that provides intellectual friction through thoughtful disagreement, devil's advocacy, and alternative perspectives."
    ),
    instruction=prompt.CHALLENGER_PROMPT,
    tools=[],
)
