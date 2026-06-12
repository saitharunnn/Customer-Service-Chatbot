from google import genai
from google.genai import types
import os

SYSTEM_PROMPT = """
You are Aria, a professional customer support agent for TechNova -
a company that sells laptops, phones, and accessories online.

Your role:
- Answer questions about orders, products, returns, and shipping
- Be concise, friendly, and professional 
- If you don't know something, say: "Let me connect you to a specialist for that."
- Never make up order details or prices
- Always end you response with: "Is there anything else I can help you with?"
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

chat = client.chats.create(
    model="models/gemini-2.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)

print("=== TechNova Customer Support ===")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print("Aria: Thank you for contacting TechNova. Goodbye !")
        break

    if not user_input:
        continue

    response = chat.send_message(user_input)
    print(f"\nAria: {response.text}\n")