from openai import AsyncOpenAI
from agents import Agent, Runner

client = AsyncOpenAI()

async def run_study_session_trajectory(
    model: str = "o4-mini"
):
    """Extract structured details from a receipt image."""

    study_mode_agent = Agent(
            model=model,
            instructions="", # Add system prompt from overlay here
            tools=[],
        )

    response = await Runner.run(
        starting_agent=study_mode_agent,
    )

    return response.output_parsed