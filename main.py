import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI as Google
import os
from langchain import PromptTemplate, LLMChain

st.title('Tweet Generator')

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
model = Google(model = "gemini-1.5-flash-latest")
tweet_template = """
Give me a tweet on {topic} in {language}.
Please follow the below instructions:
1. Make sure the tweets are not offensive.
2. The maximum word limit is 15 words.
"""
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['topic', 'language'])

topic = st.text_input("Topic: ")
number = st.number_input("Number of Tweets: ", value = 1, step = 1, max_value = 10, min_value = 1)
language = st.text_input("Language: ")

if st.button("Generate"):
    tweet_chain = tweet_prompt | model
    for i in range(number):
        response = tweet_chain.invoke({"topic": topic,
                                       "language": language})
        st.code(response.content)
