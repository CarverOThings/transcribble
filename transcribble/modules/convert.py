# Converts text files to docx files. Formats them in the process
import os
import docx
from ollama import cut_text

class DocxGenerator:
    """
    This class handles the writing of the whisper result to a cooresponding docx file.
    """

    def __init__(self, result):
        self.output_dir = os.path.abs("/home/rreel/Programming/output/")
        self.result = result

    def get_formatted(self, output_dir):
        bad_files = []
        try:
            with open(output_dir):
                for file in output_dir:
                    response = cut_text(file)
                    return response
        except FileNotFoundError as error:
            print(f"Check the output directory exists.\n {error}")
            bad_files.append(file)
            pass
        if bad_files is not None:
            print(f"Bad files: {bad_files}")

    def write_formatted(self, response):
        print(response)
    # Not sure how to handle functions here. Do I call them from inside the class? Do I define them and pull them in. At the moment I do not want to write a loop assigning these methods to seperate variables and working on them in the main functions

        

