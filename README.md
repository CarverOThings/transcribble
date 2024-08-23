# Transcribble

    > Transcribble is way to save my mother in law time by pipelining the Medical Transcription process through whisper and then llama3.

    > Openai whisper was chosen for its active development, localization to maintain patient confidentiality, ease of use and it was open source.
    >Recently added Ollama to the mix for post processing of the resulting text without any NLP modules. I found the variations in speech are difficult to catch in pure code with my abilities. Plus, I can say my app is AI transcription :)

## Explanation of Program
    
    < Transcribble takes audio files and converts them into .docx files.

    > Currently the program writes to a .txt file with plans of writing to a docx file for ease of manual postprocessing.

    > Plans for a CLI that I can pass the program a directory and it will process all those files. This will be a shared folder on out local network.

## Technical Issues 
    
    > Running the models localy is quite resource intensive. For each file to process I have to call whisper then prompt ollama. 
