import os
import eyed3

def change_metadata_and_rename(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp3"):  # Change the file extension if needed
            file_path = os.path.join(directory_path, filename)
            
            # Load metadata
            audiofile = eyed3.load(file_path)
            
            # Modify metadata as needed
            audiofile.tag.artist = "New Artist"
            audiofile.tag.album = "New Album"
            audiofile.tag.title = "New Title"
            
            # Save changes
            audiofile.tag.save()
            
            # Rename the file
            new_filename = f"{audiofile.tag.artist} - {audiofile.tag.title}.mp3"
            new_file_path = os.path.join(directory_path, new_filename)
            os.rename(file_path, new_file_path)

if name == "main":
    directory_to_process = "/path/to/your/files"
    change_metadata_and_rename(directory_to_process)
