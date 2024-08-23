from ollama import generate

def split_text(file):

    ##TODO: Add parameter size 
    with open(file, "w") as file:
        prompt = f"Please reformat the text that follows my prompt text. Do so in a way that seperates each patient entry into seperate blocks. Here is the text: {file}"

    ##TODO: add error handling.
        response = generate('llama3', prompt)
        return response
