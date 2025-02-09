from openai import OpenAI
import gradio as gr
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_structured_prompt(user_input):
    prompt = f"""
    You are an expert prompt engineer. Your task is to deeply undestand what I want, and 
    return respond with a well crafted promt, that if fed to a seperate AI, will get me exactly the 
    result I want.
    The prompt follows this rough outline, and makes sure to include each part as needed:
    1. A persona. At the start, you write somthing to the affect of „Act as an expert in...“ 
    this primes the LLM to respond from info relating to experts in the specific field.
    2. The task. This part of prompt involves exhaustively laying out the task for the LLM. It 
    is critical this part is specific and clear. This is the most important part of the 
    prompt. 
    3. Context. Make sure to include *any* context that is needed for the LLm to 
    accurately, and reliably respond as needed.
    4. Response format. Outline the ideal response format for this prompt.
    5. Examples. If needed, leave a space in the prompt for any input data. This should be 
    highlight between brackets [like this]
    Some other imporatnt notes:
    - Instruckt the model to list out it's thoughts before giving an answer.
    - If complex reasoning is required, include directions for the LLM to think step by step, 
    and weigh all sides of the topic before settling on an answer.
    - Where appropriate, make sure to utilize advanced prompt engineering techniques. 
   These include, but are not limited to: Chain of Thought, Debate simulations, self 
    restriction and Self Consistency.
    - Strickly use text, no code please.
    Please craft the perfect prompt for my request below:
    User input: "{user_input}"

    """


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    structured_response = response.choices[0].message.content
    
    return structured_response

with gr.Blocks() as chat:
    chatbot = gr.Chatbot(label="Prompt engineering agent")
    msg = gr.Textbox(placeholder="Type your message here...")
    clear = gr.Button("Clear Chat")

    def user(user_message, history):
        user_message_with_time = f"{datetime.now().strftime('%H:%M:%S')} User: {user_message}"
        return "", history + [[user_message_with_time, None]]

    def bot(history):
        user_message = history[-1][0].split("User:")[1].strip()  # Extract user message only
        bot_message = generate_structured_prompt(user_message)
        bot_message_with_time = f"{datetime.now().strftime('%H:%M:%S')} Prompt engineer: {bot_message}"

        history[-1][1] = ""
        for character in bot_message_with_time:
            history[-1][1] += character
            time.sleep(0.03) 
            yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

chat.launch()