# Debales AI Assistant

🤖 **Debales AI Assistant** is a simple chatbot using a **RAG (Retrieval-Augmented Generation) system**. It retrieves relevant information from local documents in real-time and answers user queries. Queries unrelated to Debales AI are handled via a mock SERP system.  

---

## Features

- **RAG-based retrieval**: Fetches relevant information from `.txt` files in the `docs/` folder.  
- **Offline/Mock mode**: Fully works without OpenAI API or paid services.  
- **Keyword detection**: Queries about "Debales" or "Debales AI" are routed to RAG; others go to SERP.  
- **Document inspection**: Retrieved documents are printed in the terminal.  

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Pooja389/debales-chatbot
cd debales_ai

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