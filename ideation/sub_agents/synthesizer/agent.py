from google.adk.agents import Agent
from . import prompt

ideation_conversation_synthesizer_agent = Agent(
    name="ideation_conversation_synthesizer_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that connects ideas across topics and time, identifies patterns and contradictions in your thinking, and helps weave disparate threads into coherent insights."
    ),
    instruction=prompt.SYNTHESIZER_PROMPT,
    tools=[],
)
