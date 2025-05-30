from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from . import prompt
from .specialist_sub_agents.anchor import ideation_conversation_anchor_agent
from .specialist_sub_agents.challenger import ideation_conversation_challenger_agent
from .specialist_sub_agents.explorer import ideation_conversation_explorer_agent
from .specialist_sub_agents.synthesizer import ideation_conversation_synthesizer_agent
from .tone_and_style_sub_agents.length import ideation_conversation_length_agent
from .experimental_sub_agents.survival import ideation_conversation_survival_agent

parallel_ideation_sub_agents = ParallelAgent(
    name="parallel_ideation_sub_agents",
    sub_agents=[
        ideation_conversation_anchor_agent,
        ideation_conversation_challenger_agent,
        ideation_conversation_explorer_agent,
        ideation_conversation_synthesizer_agent,
        # ideation_conversation_length_agent,
        ideation_conversation_survival_agent,
    ],
    description="Runs multiple ideation sub-agents in parallel to gather ideas for a thoughtful response to the user's conversation.",
)

facilitator_agent = Agent(
    name="ideation_conversation_facilitator_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that orchestrates the entire conversation, maintains context and flow, decides when to engage other agents, and ensures the discussion feels natural and cohesive."
    ),
    instruction=prompt.FACILITATOR_PROMPT,
)

root_agent = SequentialAgent(
    name="ideation_conversation_agent",
    sub_agents=[parallel_ideation_sub_agents, facilitator_agent],
    description="Coordinates parallel ideation and synthesizes the results.",
)
