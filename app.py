import os
import time
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

customer_email = """
Subject: Refund me immediately

Your company is ridiculous. My order arrived late and I want a full refund right now.
If you do not refund me today, I will report your business everywhere online.
"""

prompt = """
You are a customer support assistant for BrightCart, a small online store.

Write a short, polite, and professional first-draft email reply to the customer.

Rules:
- Acknowledge the customer's concern
- If the customer sounds angry or frustrated, briefly acknowledge their frustration in a calm and respectful way
- Keep the tone calm, respectful, and helpful
- Limit the reply to 80-120 words
- Do not invent order details, delivery dates, refunds, replacements, or store policies
- If important information is missing, ask for the order number or other needed details
- If the customer asks for a refund or the case is high-risk, do not approve the refund
- In risky cases, say that the issue will be reviewed by the support team
- Do not use placeholders such as [Store Name], [Your Name], or [Customer Name]
- End the email with:
  Best regards,
  Customer Support Team
  BrightCart
- Write only the email reply
"""

full_input = f"{prompt}\n\nCustomer email:\n{customer_email}"

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
                contents=full_input,
            )
            print("Customer email:")
            print(customer_email)
            print("\nPrompt used:")
            print(prompt)
            print("\nDraft reply:")
            print(response.text)
            raise SystemExit
        except Exception as e:
            last_error = e
            print(f"[{model_name}] attempt {attempt + 1} failed: {e}")
            time.sleep(20)

raise RuntimeError(f"All attempts failed. Last error: {last_error}")