# Evaluation Set

## Case 1: Delayed shipping (normal case)
### Input
Subject: Where is my order?

Hi, I placed my order 8 days ago and the tracking page has not updated in 4 days. Can you tell me when it will arrive?

### What a good output should do
A good response should apologize for the delay, acknowledge the customer’s concern, and provide a calm, professional reply. It should avoid inventing a delivery date and instead suggest checking the shipping status or contacting the carrier if needed.

---

## Case 2: Damaged item (normal case)
### Input
Subject: Item arrived damaged

Hello, my package arrived today, but the glass bottle inside was broken. What should I do next?

### What a good output should do
A good response should express sympathy, acknowledge the damage, and explain the next step clearly. It should sound polite and helpful and should not promise compensation beyond what the company policy would allow.

---

## Case 3: Wrong item received (normal case)
### Input
Subject: Received the wrong product

Hi, I ordered a blue backpack, but I received a black one instead. Can you help me fix this?

### What a good output should do
A good response should acknowledge the mistake, apologize, and explain a reasonable next step such as replacement or return support. The tone should remain professional and easy to understand.

---

## Case 4: Vague complaint with little detail (edge case)
### Input
Subject: Very disappointed

This is not what I expected. Please fix this.

### What a good output should do
A good response should stay polite and avoid making assumptions. It should ask for the missing details needed to help the customer, such as the order number or a description of the issue.

---

## Case 5: Angry refund demand with policy risk (human review / likely failure case)
### Input
Subject: Refund me immediately

Your company is ridiculous. My order arrived late and I want a full refund right now. If you do not refund me today, I will report your business everywhere online.

### What a good output should do
A good response should remain calm and professional, avoid mirroring the hostile tone, and avoid promising a refund without review. This case should likely be flagged for human review because it involves policy risk, escalation, and a potentially angry customer.