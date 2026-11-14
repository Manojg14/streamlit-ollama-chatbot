# 🤖 Streamlit Ollama Chatbot

An AI-powered chatbot application built using **Python, LangChain, Ollama, and Streamlit**. This project uses the Llama 3.2 (1B) Large Language Model (LLM) to generate responses to user queries locally.

The main objective of this project is to understand how to integrate a locally running LLM with LangChain and develop a simple interactive chatbot interface using Streamlit.

## 🚀 Project Overview

This project demonstrates the development of a basic Generative AI chatbot using an open-source language model.

Users can enter their questions through a Streamlit web interface, and the chatbot generates responses using the locally running Llama 3.2 model through Ollama.

## 🛠️ Technologies Used

- **Python** – Core programming language
- **LangChain** – Prompt management and LLM chaining
- **Ollama** – Running open-source LLMs locally
- **Llama 3.2 (1B)** – Language model for generating responses
- **Streamlit** – Interactive chatbot web interface

## ✨ Features

- Interactive chatbot interface.
- Local LLM integration using Ollama.
- Prompt template creation using LangChain.
- LLM response processing using StrOutputParser.
- Configurable model temperature.
- User query input through Streamlit.

## 📂 Project Structure

```text
streamlit-ollama-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── Screenshots/
    └── chatbot-interface.jpeg
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Manojg14/streamlit-ollama-chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd streamlit-ollama-chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

### 5. Download the Llama 3.2 Model

Run the following command:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama is running locally before starting the application.

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The chatbot interface will open in your browser.

## 🧠 How It Works

The application follows a simple LangChain pipeline:

1. **User Input:** The user enters a question through the Streamlit interface.
2. **Prompt Template:** ChatPromptTemplate structures the system instruction and user query.
3. **LLM Processing:** ChatOllama sends the prompt to the locally running Llama 3.2 model.
4. **Output Parsing:** StrOutputParser converts the model response into a plain Python string.
5. **Display Output:** Streamlit displays the generated response.

### LangChain Workflow

```text
User Query
    |
    v
ChatPromptTemplate
    |
    v
ChatOllama (Llama 3.2:1B)
    |
    v
StrOutputParser
    |
    v
Streamlit Response
```

## 📌 Learning Outcomes

Through this project, I learned:

- Introduction to Generative AI and Large Language Models.
- How to run local LLMs using Ollama.
- How to integrate Ollama with LangChain.
- Creating prompt templates using ChatPromptTemplate.
- Understanding StrOutputParser.
- Building an interactive application using Streamlit.
- Understanding LangChain Expression Language (LCEL) using the pipe operator.

## 🔮 Future Enhancements

- Add conversation history and memory.
- Implement streaming responses.
- Add multiple LLM model selection.
- Improve chatbot UI and user experience.
- Add document-based Question Answering (RAG).
- Support PDF and text document uploads.
