import argparse
import sys
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError(
        "OPENROUTER_API_KEY not found! Please make sure you have created the .env file and write the API key!"
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    max_iterations = 20
    final_response_found = False

    # Agent Loop
    for _ in range(max_iterations):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message

        if response.usage is None and args.verbose:
            print("Warning: usage is None")

        # Gunakan pengecekan aman untuk tool_calls
        if message.tool_calls:
            # 2-3. Tambahkan pesan asisten (assistant message) ke riwayat messages
            messages.append(message)

            # 6-9. Jalankan setiap tool call dan tambahkan tool messages ke riwayat
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose=args.verbose)
                
                if not result_message.get("content"):
                    raise RuntimeError("Tool execution returned empty content.")
                    
                if args.verbose:
                    print(f"-> {result_message['content']}")
                    
                messages.append(result_message)
        else:
            # Jika tidak ada tool_calls, berarti ini adalah respons final dari model
            if message.content:
                print(message.content)
            final_response_found = True
            break


if __name__ == "__main__":
    main()