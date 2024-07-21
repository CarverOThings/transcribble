def speech_to_text(file_path, model):
    # Transcribe audio file to text using the model
    print(f"Starting Audio Transcription for file {file_path}")
    try:
        result = model.transcribe(file_path)
        return result.get('text', '')  # Get text from the result, return empty string if not found
    except Exception as e:
        print(f"Error transcribing file {file_path}: {e}")
        return None