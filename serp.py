import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load API key
load_dotenv()


def serp_answer(query):
    try:
        params = {
            "q": query,
            "api_key": os.getenv("SERP_API_KEY")
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        # Extract top result snippet
        if "organic_results" in results and len(results["organic_results"]) > 0:
            return results["organic_results"][0].get("snippet", "No snippet found.")

        return "No results found."

    except Exception as e:
        return f"SERP Error: {e}"
