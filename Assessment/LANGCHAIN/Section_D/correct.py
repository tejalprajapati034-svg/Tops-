### Act as a Python and LangChain expert. Write a Python program that:
### 1. Implements a LangChain ConversationChain for a food delivery order-tracking assistant.
### 2. Uses ConversationBufferMemory.
### 3. Stores order statuses in a local Python dictionary such as:{"#101": "Preparing","#102": "Out for delivery","#103": "Delivered"}
### 4. Allows the user to enter an order ID in a terminal loop.
### 5. If the user asks "What about order #102?" after asking about another order, the assistant should use conversation memory naturally.
### 6. Exit when the user types "quit".
### 7. After exiting, print how many unique order IDs were queried during the session.
### 8. Use Python and LangChain only.


from langchain.chains.conversation.base import ConversationChain    
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
import re

orders = {
    "#101": "Preparing",
    "#102": "Out for delivery",
    "#103": "Delivered"
}

# Fixed: Explicit memory configuration
memory = ConversationBufferMemory(
    memory_key="history",
    input_key="input"
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="Gamini_api_key"
)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

queried_orders = set()

print("Food Delivery Assistant")
print("Type 'quit' to exit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    match = re.search(r"#\d+", user_input)

    if match:

        order_id = match.group()

        queried_orders.add(order_id)

        if order_id in orders:

          
            prompt = (
                f"You are a food delivery assistant. "
                f"The customer asked for order {order_id}. "
                f"The current order status is '{orders[order_id]}'. "
                f"Reply politely."
            )

        else:

          
            prompt = (
                f"Order {order_id} does not exist. "
                f"Tell the customer politely that the order ID was not found."
            )

    else:


        prompt = user_input

    response = conversation.predict(input=prompt)

    print("Assistant:", response)

print("\nSession Summary")
print("Unique Orders Queried:", len(queried_orders))