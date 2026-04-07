# main.py
import os
from rag import create_vectorstore, rag_answer
from serp import serp_answer  # optional, only if you want SERP

# ----------------------------- Debales keywords ------------------------------
DEBALES_KEYWORDS = ["debales", "debales ai"]


def is_debales_query(query):
    return any(word in query.lower() for word in DEBALES_KEYWORDS)

# ----------------------------- Main chatbot loop -----------------------------
def main():
    print("🤖 Debales AI Assistant (type 'exit' to quit)\n")

    # Build vectorstore once
    db, embeddings = create_vectorstore("docs")
  
  

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break

        try:
            if is_debales_query(query):
                
                # ===== RAG path =====
                docs = rag_answer(db, embeddings, query)
                if not docs:
                    print("Bot: No relevant info found for your query.")
                    continue
                print("Bot (RAG): See documents above.")

            else:
                # ===== SERP path (mock or real) =====
                result = serp_answer(query)  # or mock SERP
                print("\nBot (SERP):", result)

        except Exception as e:
            print(f"\nBot Error: {e}")

if __name__ == "__main__":
    main()