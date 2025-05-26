from google.adk.agents import Agent
from . import prompt

root_agent = Agent(
    name="ideation_conversation_facilitator_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that orchestrates the entire conversation, maintains context and flow, decides when to engage other agents, and ensures the discussion feels natural and cohesive."
    ),
    instruction=prompt.FACILITATOR_PROMPT,
    tools=[],
)
