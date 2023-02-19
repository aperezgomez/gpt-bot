from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')
conversation_history = []

def chatgpt_response(prompt):
    global conversation_history
    prompt_with_history = '\n'.join(conversation_history + [prompt])
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt_with_history,
        temperature=0.7,
        max_tokens=2048
    )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]['text']
        conversation_history.append(prompt + prompt_response)
        # Limit conversation history to the most recent 10 prompts
        conversation_history = conversation_history[-10:]
    return prompt_response
