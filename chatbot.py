import openai

openai.api_key = "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"

def chat_with_ai(prompt):
   response = openai.ChatCompletion.chat(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)

    return response["choices"][0]["message"]["content"]

print("Welcome to AI Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    try:
        bot_response = chat_with_ai(user_input)
        print(f"Bot: {bot_response}")
    except Exception as e:
        print(f"Bot: Error: {e}")

