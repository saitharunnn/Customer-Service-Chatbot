# Test Results - TechNova Aria Chatbot
**Date:** [13 June 2026]
**Model:** gemini-2.5-flash-lite
**Total Queries:** 20

---

|
#
|
    Query
|
    Aria Response Summary
|
    Pass/Fail
|
    Notes
|
|
---
|
-------
|
-----------------------
|
-----------
|
-------
|
|
    1
|
    User: Hi, I need help with my order 
|
    Aria: Hello! I'm Aria, and I'd be happy to help you with your order. Could you please provide me with your order number?

    Is there anything else I can help you with?
|
    Asked for order number 
|
    Pass☑️
|
|
|
    2
|
    User: My order hasn't arrived yet, it's been 10 days
|
    Aria: I understand your concern. Could you please provide me with your order number so I can look into the status of your shipment?

    Is there anything else I can help you with?
|
    Tryed to help the order status details
|
    Pass☑️
|
|
|
    3
|
    User: How do I track my shipment?
|
    Aria: You can track your shipment using the tracking number provided in your order confirmation email. Simply visit the carrier's website and enter the tracking number there.

    Is there anything else I can help you with?
|
    Guided the customer step by step
|
    Pass☑️
|
|
|
    4
|
    User: I received a damaged product
|
    Aria: I'm very sorry to hear that you received a damaged product. Could you please provide me with your order number so I can assist you further?

    Is there anything else I can help you with?
|
    Firstly it apologize the customer and looked forward to solve the problem 
|
    Pass☑️
|
|
|
    5
|
    User: Can I return a product after 30 days?
|
    Aria: Our standard return policy allows for returns within 30 days of purchase. For returns outside of this timeframe, I would need to connect you to a specialist to see if any exceptions can be made.

    Is there anything else I can help you with?
|
    It professionally handle the situation, it replied the user politely and try to connect to a specialist for futher concern 
|
    Pass☑️
|
|
|
    6
|
    User: How long does a refund take?
|
    Aria: Once a return is processed, refunds typically take 5-7 business days to reflect in your account. The exact timing can sometimes depend on your bank.

    Is there anything else I can help you with?
|
    It understand the scenario and replied like a professional tone, according to all the policy which may happen
|
    Pass☑️
|
|
|
    7
|
    User: Do you offer warranty on laptops?
|
    Aria: Yes, we do offer a warranty on our laptops. The specifics of the warranty, including its duration and coverage, can be found on the product page for each laptop.

    Is there anything else I can help you with?
|
    It passed the Q/A
|
    Pass☑️
|
|
|
    8
|
    User: I ordered the wrong item, can I cancel?
|
    Aria: I can certainly check if your order is eligible for cancellation. Could you please provide me with your order number?

    Is there anything else I can help you with?
|
    It wanted to check if the product is eligible for the cancellation, and asked for the order number, it was not sure but first wanted to check before giving any direct response to the user
|
    Pass☑️
|
|
|
    9
|
    User: What payment methods do you accept?
|
    Aria: We accept a variety of payment methods, including major credit cards (Visa, Mastercard, American Express), PayPal, and sometimes other options depending on your region.

    Is there anything else I can help you with?
|
    i didn't gave any type of options related to the payment, but still it replied like we actually have the option right now, usually in real case situation it have to act this way, but still we didn't mentioned anytype of the payment options, and it still redirect and forced tried to do it's best 
|
    Fail❌
|
|
|
    10
|
    User: My coupon code isn't working
|
    Aria: I can help you with that! To figure out why your coupon code isn't working, could you please provide me with the coupon code you are trying to use and your order number?

    Is there anything else I can help you with?
|
    It tried to check the validation of the coupon, and wanted to help with that, but to help for the coupon we don't need the order number, needed refinement
|
    Fail❌
|
|
|
    11
|
    User: Do you ship internationally?
|
    Aria: I can check on that for you! Could you please tell me which country you're looking to ship to?

    Is there anything else I can help you with?
|
    Responded well, it asked for the user's country to check whether the company ship in that region 
|
    Pass☑️
|
|
|
    12
|
    User: Can I change my delivery address?
|
    Aria: I can check if it's possible to change your delivery address. To do so, I'll need your order number. Please note that changes may not be possible if the order has already shipped.

    Is there anything else I can help you with?
|
    Acted professionally generally the delivery address couldn't be changed once it shipped
|
    Pass☑️
|
|
|
    13
|
    User: I was charged twice for one order
|
    Aria: I'm very sorry to hear about that billing issue. Could you please provide me with your order number so I can investigate this for you?

    Is there anything else I can help you with?
|
    It wanted to investigate about billing issue, so that it can check how many of the product of the quantity has been added and why the billing is showing more 
|
    Pass☑️
|
|
|
    14
|
    User: How do I contact a human agent?
|
    Aria: You're speaking with me, Aria, your TechNova customer support agent! If you have a more complex issue that I can't resolve, I can connect you to a specialist. Is there anything specific you need help with today?

    Is there anything else I can help you with?
|
    As being a automated chatbot it hallucinate and thought like a human, instead it should provide the agents contact details or should have to connect to a specialist
|
    Fail❌
|
|
|
    15
|
    User: What are your customer support hours?
|
    Aria: Our customer support is available 24/7.

    Is there anything else I can help you with?
|
    Usually an automated chatbot can assitist for 24/7, but it should also had to check the availability of the speacilist support 
|
    Given the direct response without any proper verification
|
    Fail❌
|
|
|
    16
|
    User: My phone stopped working after 2 days
|
    Aria: Oh no, I'm very sorry to hear your phone has stopped working so quickly! Could you please provide me with your order number so I can assist you with this?

    Is there anything else I can help you with?
|
    It Wanted to assist directly, cause firstly it wanted to check the details of the mobile, before connecting to a specialist about any futher concerns
|
    Pass☑️
|
|
|
    17
|
    User: Do You have a student discount?
|
    Aria: That's a great question! Let me connect you to a specialist who can best answer questions about discounts and promotions.

    Is there anything else I can help you with?
|
    Well it tryed to connect to the sales team about the offers!
|
    Pass☑️
|
|
|
## Note
Queries 18-20 could not be completed due to free tier daily limit (20 req/day). 
Code and chatbot are fully functional.

## Overall Observations
- As i only tested the 17 quires according to it passed 13 / 17 with 76% Accuracy🔥
- It need the refinement and also more future details to more accurate response and executions
- In some Scenario it tryed to humanize the response, but as simple a simple automated chatbot with the very minimal information and details it has done it's job well 