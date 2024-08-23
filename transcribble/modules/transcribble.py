from model import load_model
import os
from time import time
from utils import dir_iter, write_txt


def speech_to_text(file_path, model):
    # Transcribe audio file to text using the model
    print(f"Starting Audio Transcription for file {file_path}")
    try:
        result = model.transcribe(file_path)
        return result.get(
            "text", ""
        )  # Get text from the result, return empty string if not found
    except Exception as e:
        print(f"Error transcribing file {file_path}: {e}")
        return None


def transcribble():
    directory = "/home/rreel/Programming/transcribble/data"
    output_dir = "/home/rreel/Programming/transcribble/output"
    model = load_model()
    file_list = dir_iter(directory)
    # For each file in data directory, transcribe
    for file_name in file_list:
        # Check to make sure only audio files are processed
        if file_name.endswith(".wav"):
            # Creates our new file path to the output directory
            file_path = os.path.join(directory, file_name)
            # start timestamp
            start_time = time.time()
            # Takes the new file path for the current file and uses the model to transcribe the current audio file
            result = speech_to_text(file_path, model)
            # End timestamp
            end_time = time.time()
            # Calculate time
            elapsed_time = end_time - start_time
            print(
                f"Time elapsed since start of transcription for file {file_name}: {elapsed_time:.2f} seconds"
            )

            ## TODO: refactor this block. write_txt -> write_docx, write a func or class that handles the line splitting.
            if result:
                # Splits the filename from the extension/ mime type into a tuple. foo/bar.sh would become
                # ['foo/bar','.sh']
                base_name = os.path.splitext(file_name)[0]
                # save the text to a file and name it as somefile.txt
                write_txt(result, base_name, output_dir)

