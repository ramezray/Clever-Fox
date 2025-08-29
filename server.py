import os
import streamlit as st

from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL")
base_url = os.getenv("BASE_URL")
main_question = os.getenv("QUESTION")

client = OpenAI(
    base_url=base_url,
    api_key=openai_api_key,
)


def set_messages(question):
    messages = [{"role": "user", "content": question}]
    return messages


def generate_question():
    print("Generating question...")
    messages = set_messages(main_question)
    response = client.chat.completions.create(model=model, messages=messages)
    generated_question = response.choices[0].message.content

    st.session_state.generated_question = generated_question

    # Precompute answer
    answer_messages = set_messages(generated_question)
    answer_response = client.chat.completions.create(model=model, messages=answer_messages)
    precomputed_answer = answer_response.choices[0].message.content
    st.session_state.answer = precomputed_answer


def answer_question():
    print("Answering question...")
    generated_question = st.session_state.generated_question
    messages = set_messages(generated_question)
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    st.session_state.answer = answer
