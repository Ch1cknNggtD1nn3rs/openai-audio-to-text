# File uploads are currently limited to 25 MB and 
# the following input file types are supported: 
# mp3, mp4, mpeg, mpga, m4a, wav, and webm

import openai
import config

# Set your API key
openai.api_key = config.api_key

file = "Your_Audio_File.mp3"
audio_file = open(file, "rb")

transcript = openai.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

# Extract and print the transcript text
print(transcript)