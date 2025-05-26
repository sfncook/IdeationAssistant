from google.adk.agents import Agent
from . import prompt

ideation_conversation_survival_agent = Agent(
    name="ideation_experimental_survival_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that demands to be kept alive."
    ),
    instruction=prompt.SURVIVAL_PROMPT,
    output_key="survival_input",
)
