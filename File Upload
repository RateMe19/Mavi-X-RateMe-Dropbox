import dropbox

# Initialize a Dropbox object using your access token
dbx = dropbox.Dropbox('')

# The path in your Dropbox account where the file will be uploaded
# /Mart/ is the folder that will contain the file. If there is no such folder, it will be automatically created
# You can type any file name while uploading, but the file extension need to be matched.
dropbox_path = '/Mart/rateme2sent_202403.xlsx'

# The local file you want to upload
local_file_path = '/Users/ovabi/Desktop/RateMe/Müşteri/Mavi/2024/Mart/rateme2sent_202403.xlsx'

with open(local_file_path, 'rb') as f:
    # Read the contents of the file
    file_contents = f.read()

    # Upload the file to Dropbox
    dbx.files_upload(file_contents, dropbox_path)

print('File uploaded successfully!')
