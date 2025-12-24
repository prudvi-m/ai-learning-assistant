import os
from transcript import get_transcript
from summarizer import summarize, merge_summaries, are_videos_related

CHEATSHEET_DIR = 'cheatsheets'
os.makedirs(CHEATSHEET_DIR, exist_ok=True)

def get_topic_path(topic):
    return os.path.join(CHEATSHEET_DIR, f"{topic}.md")

def main():
    print("Welcome to the AI Learning Assistant!")
    while True:
        url = input("Enter YouTube video URL (or 'q' to quit): ")
        if url.lower() == 'q':
            break
        topic = input("Enter topic name: ")
        transcript = get_transcript(url)
        summary = summarize(transcript)
        topic_path = get_topic_path(topic)
        if os.path.exists(topic_path):
            with open(topic_path, 'r') as f:
                existing_summary = f.read()
            if are_videos_related(existing_summary, summary):
                print("Videos are related. No update needed.")
            else:
                improved = merge_summaries(existing_summary, summary)
                with open(topic_path, 'w') as f:
                    f.write(improved)
                print(f"Summary improved for topic '{topic}'.")
        else:
            with open(topic_path, 'w') as f:
                f.write(summary)
            print(f"Summary created for topic '{topic}'.")
        print("\n--- Current Cheat Sheet ---")
        with open(topic_path) as f:
            print(f.read())
        print("--------------------------\n")

if __name__ == "__main__":
    main()
