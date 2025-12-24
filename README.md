# AI Learning Assistant

This project helps you build and maintain concise, evolving cheat sheets for any learning topic using YouTube videos. It extracts transcripts, summarizes them, and lets you iteratively improve your notes by adding more videos on the same topic.

## Features
- Extracts transcript from YouTube videos
- Summarizes content into short notes
- Maintains a cheat sheet per topic (in `cheatsheets/`)
- Allows you to add more videos to improve or update the summary
- Detects if a new video is related to the existing summary

## Requirements
- Python 3.8+
- OpenAI API key (for summarization)

## Installation
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd ai-learning-assistant
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable:
   ```sh
   export OPENAI_API_KEY=sk-...your-key...
   ```

## Usage
Run the assistant:
```sh
python main.py
```

Follow the prompts:
- Enter a YouTube video URL and a topic name.
- The assistant will extract the transcript, summarize it, and create or update the cheat sheet for that topic.
- Add more videos on the same topic to improve your notes.

Cheat sheets are saved as markdown files in the `cheatsheets/` directory.

## Notes
- Only public YouTube videos with available transcripts are supported.
- Summarization uses OpenAI's GPT-3 (or compatible) API.
- You can customize the summarization logic in `summarizer.py`.

## Example
```
Enter YouTube video URL (or 'q' to quit): https://www.youtube.com/watch?v=abcd1234
Enter topic name: Data Structures
Summary created for topic 'Data Structures'.

--- Current Cheat Sheet ---
...summary content...
--------------------------
```

## License
MIT
