import os
from os import path
import whisper
 
# set the relative directory
directory = os.path.join(path.dirname(path.realpath(__file__)), "../dictation")

def load_model():# loads the whisper model in memory for use later on each iteration through directory
    return whisper.load_model("medium.en")
 
def dir_iter(directory):# returns a list of files within directory
    file_list = os.listdir(directory)
    print("Found {len(file_list)} audio files.")
    return file_list

def speech_to_text(file, model): #Function to convert audio to text. Returns text
        print("Starting Audio Transcription for file {file}", file)
        try:
            result = model.transcribe(file_list[i])# transcribe the current file 
            return result
        except Exception as e:
            print(f"Error transcribing file {file}: {e}")
            return None


def write_result(result, file):
    output_dir = "../output" # name of output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 

    for file_name in file_list: #loops through file list
                if file_name.endswith(".wav"): #validates the file extensition
                    base_name = os.path.splitext(file_name)[0] # splits string into list and removes the .wav file extension by assigning just the file name to a variable.
                    txt_file_name = base_name + ".txt" #Creates the file name with the corrext extension ###TODO change this to a .docx file later on
                    txt_file_path = os.path.join(output_dir, txt_file_name) # Final file path for the new file
                    with open(txt_file_path, "w") as txt_file:
                        try:
                            txt_file.write(result)
                        except:
                            print("Error writing to file.")
                            exit()

def main():
    model = load_model() #Load model/ Returns whisper model  
    for file in dir_iter(): # Read files from input directory/ Returns a file list
        for i in file_list:
            result = speech_to_text() # transcribe the current audio file into a variable
            write_result(result, file) # write the result
            
if __name__ == "__main__":
    main()
