import dropbox

# Initialize a Dropbox object using your access token
dbx = dropbox.Dropbox('')

# You can choose the path of the folder you want to see the files inside it. 
# You can also view all the folders and files inside the Dropbox by inserting only ''
folder_path = '/Mart/'

try:
    # List the contents of the folder
    response = dbx.files_list_folder(folder_path)

    # Loop through each entry (files and subfolders) and print details
    for entry in response.entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            size_mb = entry.size / 1048576  # Convert bytes to megabytes
            print(f"File: {entry.name}, Size: {size_mb:.2f} MB")
        elif isinstance(entry, dropbox.files.FolderMetadata):
            print(f"Folder: {entry.name}")
except Exception as e:
    print(f"Error: {e}")
