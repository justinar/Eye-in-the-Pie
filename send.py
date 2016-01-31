import dropbox 
import glob, os

access_token = 'xd6q_9NhInAAAAAAAAADsWfPIRXdExzs3Lj1R5iltdYE5iAT45UIB4NXUi4Z9nRg'
client = dropbox.client.DropboxClient(access_token)

print 'linked account', client.account_info()

for file in os.listdir('scanned'):
	if file.endswith('.nettxt'):
		f = open('scanned/'+ file, 'rb')
		response = client.put_file(f.name , f) 
