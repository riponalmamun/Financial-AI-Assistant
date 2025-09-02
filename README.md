# 🚀 Intelligent Financial AI Assistant with PhiData

This project implements a smart financial AI assistant capable of providing real-time stock prices, fundamental analysis, analyst recommendations, and company news using multi-agent AI models and integrated financial tools.

# Features

Multi-Agent Architecture

Financial Agent: Specialized in stock and financial data.

Main Assistant: Delegates queries to the Financial Agent or handles web search.

Web Search Agent: Uses DuckDuckGo to retrieve general information.

# AI Models

Groq Models: llama-3.1-8b-instant, mixtral-8x7b-32768, gemma-7b-it with fallback support.

HuggingFace Models: For general web search queries.

# Financial Tools

YFinance: Fetch real-time stock prices, fundamentals, analyst recommendations, and company news.

Interactive Web Playground

Built with PhiData Playground and FastAPI.

Supports live queries, multi-agent collaboration, and markdown/table outputs.

Modular Design

Agents are reusable and can be imported into other scripts or playgrounds.

# Tech Stack

Python 3.13+

PhiData Playground

Groq API

HuggingFace Transformers

YFinance

FastAPI / Uvicorn

Installation

Clone the repository

```bash
git clone https://github.com/yourusername/financial-ai-assistant.git
cd financial-ai-assistant
```

Create a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Linux/macOS
```

Install dependencies
```bash
pip install -r requirements.txt
```

Set up environment variables

Create a .env file with:
```bash
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key
HF_API_KEY=your_huggingface_api_key
```

Running the Financial Agent
```bash
python financial_agent.py

```
Interact with the financial AI in the terminal.

Type exit to quit.

Running the Playground
```bash
python playground.py

```


Opens a web-based interface at http://localhost:7777.

Use the live demo URL (ngrok or PhiData hosted) to share with others.


Example Queries

"What is the current stock price of AAPL?"

"Show me the latest financial fundamentals for Microsoft."

"Compare the P/E ratio of AAPL, MSFT, and GOOGL."

"Get AAPL stock price and recent news about Tesla."

Optional: Share a Live Demo

Use ngrok to make your Playground accessible online:
```bash
pip install pyngrok
ngrok http 7777
```

# Screenshots / Demo

<img width="1918" height="911" alt="3" src="https://github.com/user-attachments/assets/c16eacae-8cfd-4432-9025-6a7c5edc8af9" />
<img width="1916" height="910" alt="4" src="https://github.com/user-attachments/assets/bee52374-dde3-473b-a78f-c6c45d7674f2" />
<img width="1627" height="612" alt="1" src="https://github.com/user-attachments/assets/3d329f09-1615-4603-bc75-cb8e6c95a995" />






