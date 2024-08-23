import whisper

from transcribble.modules.checks import gpu_available


def load_model():
    if gpu_available():
        # Load and return the Whisper model
        return whisper.load_model("medium.en")


class Model:
    # Pytorch check. will return True if a gpu is available, False if not
    def __init__(self):
        self.model = load_model()
