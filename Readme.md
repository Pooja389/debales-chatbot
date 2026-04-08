# Debales AI Assistant

🤖 **Debales AI Assistant** is a simple chatbot that combines **RAG (Retrieval-Augmented Generation)** and **SERP-based search**. It retrieves relevant information from local documents for Debales-related queries and uses real-time web search for general queries, providing accurate and context-aware responses.

---

## Features

- **Hybrid RAG + SERP system**: Uses RAG for document-based queries and SERP for real-time web search.  
- **RAG-based retrieval**: Fetches relevant information from `.txt` files in the `docs/` folder.  
- **SERP integration**: Handles general queries using search results for up-to-date information.  
- **Offline/Mock mode**: Can run without OpenAI or paid APIs (RAG works locally).  
- **Keyword-based routing**: Queries related to "Debales" are routed to RAG; others go to SERP.  
- **Document inspection**: Retrieved documents are displayed in the terminal for transparency.  
---
## Note

This project is developed and tested using **Python 3.11**.  
It is recommended to use Python 3.11 for compatibility, as some dependencies may not work properly with newer versions (e.g., Python 3.13+).
## Setup

Steps to run:

```bash
git clone https://github.com/Pooja389/debales-chatbot

```
```bash
cd debales-chatbot
```
  imp : create a .env file in debales-chatbot folder and paste your serp_api --> SERP_API_KEY = 'Your_key'
```bash
pip install -r requirements.txt
```
```bash
python main.py
```

## Example Usage

```text
🤖 Debales AI Assistant (type 'exit' to quit)

You: what is Debales AI

--- Retrieved Documents ---
Doc 1: Debales AI is an example of RAG-based retrieval system...
--------------------------

Bot (RAG): See documents above.

You: what is a mouse

Bot (SERP): A computer mouse is a hand-held device used to move the cursor on a screen.

You: exit

Bot: Goodbye 👋
