from openai import OpenAI
import gradio as gr

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)


def generate_response(prompt):
    response = client.chat.completions.create(
        model="qwen2:0.5b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def interact(message, history):
    return generate_response(message)

gr.ChatInterface(interact).launch()
