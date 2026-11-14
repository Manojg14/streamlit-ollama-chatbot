from langchain_core.prompts import ChatPromptTemplate # This template for chatbot application
from langchain_core.output_parsers import StrOutputParser # Sometimes model generates symbols like /n... like that, if we use output_parsers means it will be cancelled it 
from langchain_ollama import ChatOllama
import streamlit as st

st.title("Manoj's Show Chat Bot")
input_txt = st.text_input("Please enter your queries here....")

prompt = ChatPromptTemplate.from_messages(
    [("system", "Your are a helpful AI Assistant."),
     ("human", "User query:{query}")
    ])

llm = ChatOllama(model="llama3.2:1b",temperature=0.7)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"query":input_txt})) 
    