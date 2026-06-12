# Learning Notes

## Concepts I learned for This project

### 1. System Prompt
- Instructions given to the model before conversation starts
- Defines persona, tone, boundaries
- Directly controls response quality

### 2. API Flow
User input → Python script → Gemini API → response → terminal

### 3. Message Roles
- system: who the bot is 
- user: what the customer says
- assistant: what the bot replied (history)

### 4. Chat sessions
- google-genai SDK maintains history automatically
- Each send_message includes full context

## Key insight
A system prompt is the most powerful tool in applied AI.
Same model, different prompt = completely different product