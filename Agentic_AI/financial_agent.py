import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not set. Please add it to your environment or .env file.")

# -----------------------------
# Helper: Get a working Groq model
# -----------------------------
def get_groq_model():
    """Try multiple Groq models until one works"""
    models = ["llama-3.1-8b-instant", "mixtral-8x7b-32768", "gemma-7b-it"]
    for model_id in models:
        try:
            return Groq(id=model_id)
        except Exception as e:
            print(f"⚠️ Model {model_id} failed: {e}")
    raise RuntimeError("❌ No available Groq models found. Check Groq docs.")

# -----------------------------
# Initialize tools (reuse for both agents)
# -----------------------------
yfinance_tools = YFinanceTools(
    stock_price=True,
    analyst_recommendations=True,
    stock_fundamentals=True
)

# -----------------------------
# Define agents
# -----------------------------
financial_agent = Agent(
    name="Financial Agent",
    role="Get financial data and stock information",
    model=get_groq_model(),
    tools=[yfinance_tools],
    instructions=["Provide accurate financial data and analysis"],
    show_tool_calls=False,
    markdown=True,
)

main_agent = Agent(
    name="Main Assistant",
    model=Groq(id="llama-3.1-8b-instant"),
    team=[financial_agent],
    tools=[yfinance_tools],  # allow main agent to call financial tools
    instructions=[
        "You are a financial assistant. Use the financial agent or tools to get stock prices, fundamentals, and analysis."
    ],
    show_tool_calls=False,
    markdown=True,
)

# -----------------------------
# Function to get agents for import
# -----------------------------
def get_agents():
    """Return initialized financial_agent and main_agent"""
    return financial_agent, main_agent

# -----------------------------
# CLI interface (runs only when executed directly)
# -----------------------------
if __name__ == "__main__":
    print("🤖 Welcome to the Financial AI Assistant!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Run Financial Agent
        try:
            print("\n💹 Financial Agent:")
            financial_agent.print_response(user_input, stream=True)
        except Exception as e:
            print(f"⚠️ Financial Agent failed: {e}")

        # Run Main Agent
        try:
            print("\n🤖 Main Agent (combined):")
            main_agent.print_response(user_input, stream=True)
        except Exception as e:
            print(f"⚠️ Main Agent failed: {e}")

        print("\n" + "="*80 + "\n")
