import openai  

# Replace 'your-api-key' with your actual OpenAI API key
OPENAI_API_KEY = "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"

def chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
