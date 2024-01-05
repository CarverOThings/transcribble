# Dictation Automation

    > Project started as a way to save my MIL time by pipelining the Medical Transcription process through whisper.

    > Openai whisper was chosen for its active development, localization to maintain patient confidentiality, ease of use and it was open source.  

## Explanation of Program
    
    < src/main.py handles all of the program logic at the moment. In the sub 100 lines of python, the model is loaded only once, the program gets a file list from 
    a relative input directory, transcribes each file in iteration and writes the resulting text to a .txt file.

    > Currently the program writes to a .txt file with plans of writing to a docx file for ease of manual postprocessing.

    > further plans to add a gui or webgui for UX but for now the user will be placing all the audio files in the input folder, running the program,
    doing literally anything else, then coming back and validating accuracy for manual postprocessing from the output directory.

## Technical Issues 
    
    > While Pytorch supports ROCM, ROCM does not support my AMD RX6600xt gpu. My Ryzen 5 2600 cpu struggles with the medium <= language models. Looking at
    Huggingface transformers to deply batch work on the model itself. And maybe if I hit the lottery or a long lost uncle leaves me loads of cash I will
    buy a 7900xtx gpu and forget about it.
