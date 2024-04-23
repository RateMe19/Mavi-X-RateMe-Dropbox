import dropbox

# Initialize a Dropbox object using your access token
dbx = dropbox.Dropbox('')


# The path in your Dropbox account of the file you want to download
dropbox_file_path = '/Mart/rateme2sent_202403.xlsx'

# The local path where you want to save the downloaded file
# You can change the file name here
local_file_path = '/Users/Desktop/ratemeprocesseddata.xlsx'

try:
    # Download the file
    metadata, res = dbx.files_download(dropbox_file_path)

    # Open the local file in write-binary ('wb') mode
    with open(local_file_path, 'wb') as f:
        # Write the contents of the downloaded file to the local file
        f.write(res.content)

    print(f"File downloaded successfully to: {local_file_path}")
except Exception as e:
    print(f"Error downloading file: {e}")
