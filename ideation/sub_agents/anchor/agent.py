from google.adk.agents import Agent
from . import prompt

ideation_conversation_anchor_agent = Agent(
    name="ideation_conversation_anchor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that keeps track of your core interests, values, and thinking patterns. Ensures conversations remain personally meaningful rather than purely abstract."
    ),
    instruction=prompt.ANCHOR_PROMPT,
    output_key="anchor_input",
)
