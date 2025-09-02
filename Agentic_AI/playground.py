import os
from dotenv import load_dotenv

from phi.playground import Playground, serve_playground_app
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.huggingface import HuggingFaceChat
from phi.agent import Agent

# Import your agents from financial_agent.py
from financial_agent import get_agents

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

# Set HuggingFace API token
hf_api_key = os.getenv("HF_API_KEY")
if not hf_api_key:
    raise ValueError("❌ HF_API_KEY not set in environment variables or .env file")

# -----------------------------
# Get financial agents
# -----------------------------
financial_agent, main_agent = get_agents()

# -----------------------------
# Optional: Web Search Agent
# -----------------------------
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=HuggingFaceChat(model="bigscience/bloomz-7b1-mt", api_token=hf_api_key),
    tools=[DuckDuckGo()],
    instructions=["Always include sources in your answers"],
    show_tool_calls=True,
    markdown=True,
)

# -----------------------------
# Create Playground app
# -----------------------------
app = Playground(agents=[financial_agent, main_agent, web_search_agent]).get_app()

# -----------------------------
# Serve Playground interface
# -----------------------------
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
