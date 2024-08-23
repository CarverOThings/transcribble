import os


def write_txt(text, base_name, output_dir):
    # Write transcription result to a .txt file
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    txt_file_path = os.path.join(output_dir, f"{base_name}.txt")
    with open(txt_file_path, "w") as txt_file:
        txt_file.write(text)
        return txt_file_path


def dir_iter(directory):
    # List all files in the directory and print the count
    file_list = os.listdir(directory)
    print(f"Found {len(file_list)} audio files.")
    return file_list
