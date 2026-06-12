# TechNova Customer Service Chatbot

An AI-powered customer support chatbot built with Python and the Gemini API.

## What it does
- Acts as "Aris", a support agent for TechNova
- Handles orders, returns, shipping, and product queries
- Maintains conversation history within a session
- Runs interactively in the terminal

## Tech Stack
- Python 3.14
- Google Gemini API (gemini-2.5-flash-lite)
- google-genai SDK

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-genai
export GEMINI_API_KEY="your-key-here"
python3 customer_service_bot.py
```

## Project Structure
customer-service-chatbot/
├── customer_service_bot.py   # chatbot script
├── build_report.md           # How it was built
├── test_results.md           # 17 query results
├── day4_notes.md             # Learning notes
└── README.md

## Test Results 
- 17 queries tested
- 13/17 passed (76% accuracy)
- Fails mostly due to lack of real order/product data

## What I'd improve next 
- Add real product/pricing data to system prompt
- Add error handling for rate limits
- Build a simple web UI with Streamlit