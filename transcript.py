from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url):
    # Extract video ID from URL
    import re
    match = re.search(r"v=([\w-]+)", url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    video_id = match.group(1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([entry['text'] for entry in transcript])
    return text
