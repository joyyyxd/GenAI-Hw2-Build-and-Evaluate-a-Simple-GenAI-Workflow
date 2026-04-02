import os
import time
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

customer_email = """
Subject: Where is my order?

Hi, I placed my order 8 days ago and the tracking page has not updated in 4 days.
Can you tell me when it will arrive?
"""

prompt = f"""
You are a customer support assistant for a small online store.

Write a polite and professional first-draft email reply to the customer.

Rules:
- Acknowledge the customer's concern
- Keep the tone calm and helpful
- Do not invent order details or delivery dates
- If important information is missing, ask for it
- Write only the email reply, not multiple options

Customer email:
{customer_email}
"""

models_to_try = [
    "gemini-3.1-flash-lite-preview",
    "gemini-3-flash-preview",
]

last_error = None

for model_name in models_to_try:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            print("Customer email:")
            print(customer_email)
            print("\nDraft reply:")
            print(response.text)
            raise SystemExit
        except Exception as e:
            last_error = e
            print(f"[{model_name}] attempt {attempt + 1} failed: {e}")
            time.sleep(20)

raise RuntimeError(f"All attempts failed. Last error: {last_error}")