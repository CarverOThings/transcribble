import os
import time
from modules.model import load_model
from modules.transcrible import speech_to_text
from modules.utils import dir_iter, write_result

def main():
    directory = "/home/rreel/Programming/transcribble/data"
    output_dir = "/home/rreel/Programming/transcribble/output"
    model = load_model()
    file_list = dir_iter(directory)
    for file_name in file_list:
        if file_name.endswith(".wav"):
            file_path = os.path.join(directory, file_name)
            # start timestamp
            start_time = time.time()
            result = speech_to_text(file_path, model)
            # End timestamp
            end_time = time.time()
            #Calculate time 
            elapsed_time = end_time - start_time
            print(f"Time elapsed since start of transcription for file {file_name}: {elapsed_time:.2f} seconds")

            if result:
                base_name = os.path.splitext(file_name)[0]
                write_result(result, base_name, output_dir)

if __name__ == "__main__":
    main()
