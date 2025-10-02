from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools

agent = Agent(
    model=OpenAIChat(),
    tools=[HackerNewsTools()],
    markdown=True,
)
agent.print_response("Summarize the top 5 stories on hackernews")
