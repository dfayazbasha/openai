import openai

openai.api_key = "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"

def chat_with_bot(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_response = chat_with_bot(user_input)
    print(f"Bot: {bot_response}")
