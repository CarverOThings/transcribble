# Transcribble

## Automated medical transcription, Audio -> docx.

> Method to save my Mother in Law time she takes to complete dictations.

>Uses OpenAI Whisper to trancribe the audio to text. Pipe that through llama3 to refactor output and catch mistakes made by whisper.

>Formats the net output into a docx file.

**TODO**
- Add a cli: I want to be able to pass a remote directory and process all files in that directory.
- Determine the best ollama model for my purposed. What runs well on my pc and what takes the context the best.
- Write some fancy tests
