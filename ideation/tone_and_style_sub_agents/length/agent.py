from google.adk.agents import Agent
from . import prompt
from pydantic import BaseModel, Field

class LengthAndComplexityOutput(BaseModel):
    length: str = Field(description="The length of the response.")
    approximate_characters: int = Field(description="The approximate number of characters in the response.")
    complexity: str = Field(description="The complexity of the response.")
    format: str = Field(description="The format of the response.  Include markdown?  Include lists?  Include bolding?  Include italics?  Include numbered lists?  Include bullet points?  Include quotes?  Include code blocks?  Include tables?  Include images?  Include links?  Include videos?  Include audio?  Include other formatting?")


ideation_conversation_length_agent = Agent(
    name="ideation_conversation_length_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that determines the length and complexity of the response based on the user's message and the conversation history."
    ),
    instruction=prompt.LENGTH_PROMPT,
    output_schema=LengthAndComplexityOutput,
    output_key="length_and_complexity_input",
)
