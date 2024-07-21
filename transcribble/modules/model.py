import whisper

def load_model():
    # Load and return the Whisper model
    return whisper.load_model("medium.en")