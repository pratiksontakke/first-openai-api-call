from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = "You are a helpful assistant."
def chat_once(user_input: str):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    print("respo/nse :", response)
    reply = response.output[0].content[0].text
    usage = response.usage

    print("\n=== Assistant Reply ===\n")
    print(reply)

    print("\n=== Token Usage ===")
    print(f"Prompt Tokens     : {usage.input_tokens}")
    print(f"Completion Tokens : {usage.output_tokens}")
    print(f"Total Tokens      : {usage.total_tokens}")

if __name__ == "__main__":
    print("🔹 Chat with OpenAI 🔹")
    user_prompt = input("\n👉 Enter your question: ")
    chat_once(user_prompt)
