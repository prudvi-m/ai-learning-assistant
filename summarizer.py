import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize(text):
    # Replace with your preferred LLM or summarizer
    prompt = f"Summarize the following content in short notes:\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def are_videos_related(existing_summary, new_summary):
    # Simple check: if summaries are very similar, consider related
    return new_summary[:100] in existing_summary

def merge_summaries(existing_summary, new_summary):
    # Naive merge: append new summary if not already present
    if new_summary not in existing_summary:
        return existing_summary + "\n\n" + new_summary
    return existing_summary
